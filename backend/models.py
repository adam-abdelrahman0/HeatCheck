import tensorflow as tf
from tensorflow.keras.models import load_model

import numpy as np

import cv2

import base64

from imageCutting.cutImages import resize_and_pad, process

import json

# os.environ['CUDA_VISIBLE_DEVICES'] = '-1'

model = load_model("./training/heatcheck-dense.keras")
# https://github.com/facebookresearch/detectron2.git@c69939aa85460e8135f40bce908a6cddaa73065f

def getHeat(image):
    # put the image into an opencv image
    data = image.split(',')[1]
    npArray = np.fromstring(base64.b64decode(data), np.uint8)
    image = cv2.imdecode(npArray, cv2.IMREAD_COLOR)

    image = process(image, "nothing")
    if type(image) == type(-1):
        return "no human"
    
    output = model(np.array([image]))

    # use how close they got to any particular style to determine their heat score
    maximum = np.max(output)
    print(maximum)
    return str(212*maximum)