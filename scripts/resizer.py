## Bulk image resizer

# Usage: place this script in a folder of images you want to shrink,
# and then run it.

import numpy as np
import cv2
import os

dir_path = os.getcwd()

for filename in os.listdir(dir_path):
    
    if filename.startswith("2018"):
        image = cv2.imread(filename)
        resized = cv2.resize(image,None,fx=0.125, fy=0.125, interpolation=cv2.INTER_AREA)
        cv2.imwrite(filename,resized)
