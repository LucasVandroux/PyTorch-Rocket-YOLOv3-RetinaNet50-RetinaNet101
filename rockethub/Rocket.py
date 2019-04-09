import tarfile
import os
import importlib
import types
import requests
from tqdm import tqdm
from .DiscoveryAPI import DiscoveryAPI
from datetime import datetime

def unpack_archive(path: str):
    ensure_dir('rockets')
    t = tarfile.open(path, 'r')
    model_name = os.path.commonprefix(t.getnames())
    t.extractall('rockets')
    os.remove(path)

    return model_name


def ensure_dir(dir_name: str):
    """Creates folder if not exists.
    """
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)

class Rocket:

    @staticmethod
    def land(rocket: str, folder_path = 'rockets', chunk_size = 512):
        """ Download or check that the Rocket is ready locally

        Download the Rocket if it is not yet locally here.

        Args:
            rocket (str): Rocket identifier (author/name/(version))
            folder_path (str): folder where to check if the Rocket is here already or where to download it
            chunk_size (int): size of the chunk when downloading the Rocket
        """
        
        # Check if the rocket exists and get the last version if not precised
        rocket_author, rocket_name, rocket_version = DiscoveryAPI().get_rocket_info(rocket)

        # Check if folder to download the rockets exists
        ensure_dir(folder_path)
        
        # Check if the rocket has already been downloaded
        rocket_folder = DiscoveryAPI().get_rocket_folder(rocket_author, rocket_name, rocket_version)

        if rocket_folder in os.listdir(folder_path): 
            model_name = rocket_folder
            print('Rocket is already here.')
        
        else:
            # Get the rocket's url
            url = DiscoveryAPI().get_rocket_url(rocket_author, rocket_name, rocket_version)
            path_to_landing_rocket = os.path.join(folder_path, 'landing_rocket.tar')

            #Download URL
            print('Rocket in approach...')
            h = requests.head(url, allow_redirects=True)
            headers = h.headers
            content_type = headers.get('content-type')
            content_length = int(headers.get('content-length', None))
            # print('content-type', content_type)

            response = requests.get(url, stream=True)
            
            pbar = tqdm(total=content_length, ascii=True, desc='Rocket Landing')
            with open(path_to_landing_rocket, 'wb') as handle:
                for data in response.iter_content(chunk_size = chunk_size):
                    handle.write(data)
                    # update the progress bar
                    pbar.update(chunk_size)
            
            pbar.close()
            
            model_name = unpack_archive(path_to_landing_rocket)
            print('It is a sucess! The Rocket has landed!')

        print("Let's build the Rocket...")
        #Build the model
        module = importlib.import_module('rockets.{}.rocket_builder'.format(model_name))
        build_func = getattr(module, 'build')
        model = build_func()
        print("The Rocket is ready for use!")
        return model



