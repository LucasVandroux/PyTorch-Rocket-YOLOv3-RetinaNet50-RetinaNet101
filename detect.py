import torch
from torch.autograd import Variable
from rockethub.Rocket import Rocket
from PIL import Image

# --- LOAD IMAGE ---
# Select the image you want to test the Object Detection Model with
image_path = 'images/office.jpg'
# image_path = 'images/shop.jpg'
# image_path = 'images/street.jpg'

img = Image.open(image_path)

# --- LOAD ROCKET ---
# Select the Rocket you want to test
rocket = "lucas/ssd"
# rocket = "igor/retinanet"
# rocket = "lucas/yolov3"

model = Rocket.land(rocket)
model.eval()

# --- DETECTION ---
with torch.no_grad():
    img_tensor = model.preprocess(img)
    out = model(Variable(img_tensor))

# --- OUTPUT ---
# Print the output as a JSON
bboxes_out = model.postprocess(out, img)
print(bboxes_out)

# Display the output over the image
img_out = model.postprocess(out, img, visualize=True)
img_out.save("out.png")


