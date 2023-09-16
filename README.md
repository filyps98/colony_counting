# Colony Counting

## Goal of the Project
This program processes images of Petri dishes to highlight colonies present inside.

First, the petri disk is isolated from the rest of the images, then the following Petri dish agars are used and they are divided into the type of strategy employed:

1. CHOCV, MRSA, CNA & MCK: Transform the image to HSV and extract the saturation component, invert white with black, apply background subtraction, blur the image, and apply a binary and otsu threshold to further highlight the colonies. 
   
2. CLED: Remove the label on the bottom of the Petri dish without getting rid of colonies, apply background subtraction, blur the image, and apply a binary and otsu threshold. 

3. CPSE: Transform the image to HSV and extract the hue and saturation component, if the saturation component is mostly black we use the hue component, invert white with black, apply background subtraction, blur the image, and finally apply a binary and otsu threshold. If the saturation component is mostly white, we apply the same procedure but with the saturation component instead of hue.

## How to use

### Set-up
Install the following libraries for image processing:
''' python
import cv2
import numpy as np
import skimage.filters import try_all_threshold
from skimage.restoration import inpaint
import math
import matplotlib.pyplot as plt'''

The following is for exploring the image directory
''' python
import os
import glob'''

### Start the program
Type '''python python main.py''' to start the program and choose the image and the respective agar employed to calculate the number of colonies in a petri dish. 

