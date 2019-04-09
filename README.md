# RocketHub Tutorial #1
    Have you ever wanted to test multiple Deep Learning models and compare their results very easily?

    Are you tired of picking a Deep Learning model just because it is the only one you are able to run?

We want to solve this problem and we packaged 3 state-of-the-art Deep Learning models for Object detection for you to easily test them.

We are calling those new way of packaging Deep Learning models: __Rockets__.

__Welcome to the Rockets Builder Community!!!__

## Install the python dependencies
```
# Python 3.5.2
python3 -m virtualenv .env
source .env/bin/activate
pip install -r requirements.txt
```
## A Tale of 3 Rockets
For this first tutorial, we selected three state-of-the-art models for you to play with:
1. SSD: Single Shot MultiBox Detector ___[[paper]](https://arxiv.org/pdf/1512.02325.pdf)___
2. RetinaNet ___[[paper]](https://arxiv.org/pdf/1708.02002.pdf)___
3. YOLOv3 ___[[paper]](https://pjreddie.com/media/files/papers/YOLOv3.pdf)___

## Run the Object Detection model
Everything is happening in the `detect.py` file. There you can choose which image and model to use with juste one line of code.

Once you are ready you just need to run `python detect.py` and everything will happen magically.

Don't hesitate to play around by swapping the different Rockets and comparing their output.

## Contact
Any feedback or complaint from your neighbors about the noise your Rockets are making, please contact us at [hello@mirage.id](mailto:hello@mirage.id). 