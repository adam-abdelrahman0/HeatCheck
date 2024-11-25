import torch, detectron2
TORCH_VERSION = ".".join(torch.__version__.split(".")[:2])
CUDA_VERSION = torch.__version__.split("+")[-1]
print("torch: ", TORCH_VERSION, "; cuda: ", CUDA_VERSION)
print("detectron2:", detectron2.__version__)

# COMMON LIBRARIES
import os
import cv2

from datetime import datetime

# DATA SET PREPARATION AND LOADING
from detectron2.data.datasets import register_coco_instances
from detectron2.data import DatasetCatalog, MetadataCatalog

# VISUALIZATION
from detectron2.utils.visualizer import Visualizer
from detectron2.utils.visualizer import ColorMode

# CONFIGURATION
from detectron2 import model_zoo
from detectron2.config import get_cfg

# EVALUATION
from detectron2.engine import DefaultPredictor

# TRAINING
from detectron2.engine import DefaultTrainer

import numpy as np

import threading

cfg = get_cfg()
cfg.merge_from_file(model_zoo.get_config_file("COCO-InstanceSegmentation/mask_rcnn_R_50_FPN_3x.yaml"))
cfg.MODEL.ROI_HEADS.SCORE_THRESH_TEST = 0.5
cfg.MODEL.WEIGHTS = model_zoo.get_checkpoint_url("COCO-InstanceSegmentation/mask_rcnn_R_50_FPN_3x.yaml")
predictor = DefaultPredictor(cfg)


local_download_path = os.path.expanduser('/media/cnie109/Backup Plus/HeatCheckImages-Full') #replace path with the directory of images
# local_download_path = os.path.expanduser('/home/cnie109/Documents/codeStuff/python/heatcheck/imageCutting/images') #replace path with the directory of images


def resize_and_pad(image, target_size):
    h, w = image.shape[:2]
    target_w, target_h = target_size

    # Calculate the new size while maintaining aspect ratio
    scale = min(target_w / w, target_h / h)
    new_w = int(w * scale)
    new_h = int(h * scale)

    # Resize the image
    resized_image = cv2.resize(image, (new_w, new_h))

    # Create a white background for padding
    padded_image = np.ones((target_h, target_w, 3), dtype=np.uint8) * 255  # White background

    # Calculate padding (center the image)
    x_offset = (target_w - new_w) // 2
    y_offset = (target_h - new_h) // 2

    # Place the resized image onto the white background
    padded_image[y_offset:y_offset + new_h, x_offset:x_offset + new_w] = resized_image

    return padded_image

def process(image, imageName):
  image = resize_and_pad(image, (512, 512))
  outputs = predictor(image)

  masks = outputs["instances"].pred_masks
  person_mask = masks[outputs["instances"].pred_classes == 0]

  if len(person_mask) > 0:
    combined_mask = torch.sum(person_mask, dim=0).cpu().numpy()
    combined_mask = (combined_mask > 0).astype(np.uint8)  #convert to binary mask

    white_background = np.ones_like(image) * 255  #a white image

    # Create the inverse mask for background (0 for person, 1 for background)
    inverse_mask = cv2.bitwise_not(combined_mask)

    # Place the original subject over the white background
    subject = cv2.bitwise_and(image, image, mask=combined_mask)  # Keep the subject using the mask
    background = cv2.bitwise_and(white_background, white_background, mask=inverse_mask)  # Keep the white background

    # Combine subject with the white background
    result = cv2.add(subject, background)
    
    subject = resize_and_pad(subject, (128, 128))
    #save result
    cv2.imwrite("/media/cnie109/Backup Plus/HeatCheckImages-Full-cut-small/" + imageName, subject) #replace with output folder
    # cv2.imwrite("/home/cnie109/Documents/codeStuff/python/heatcheck/imageCutting/cutImages/" + imageName, subject) #replace with output folder

    #subject = cv2.imread("./output_images/" + imageName, cv2.IMREAD_UNCHANGED)
    #cv2_imshow(subject)

def f(filename):
        image = cv2.imread(local_download_path + "/" + filename)
        threading.Thread(process(image, filename)).start()


data = []
count = 0

for filename in os.listdir(local_download_path):
    if filename.endswith("jpg") or filename.endswith("jpeg"):
        # Your code comes here such as
        data.append(filename)

        # image = cv2.imread(local_download_path + "/" + filename)
        # #cv2_imshow(image)
        # threading.Thread(process(image, filename)).start()
        threading.Thread(f(filename)).start()
        count += 1
        print("count is now", count)