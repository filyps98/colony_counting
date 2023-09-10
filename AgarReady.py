#Algorithm illustrating actions needed for each specific agar, incomplete results cause specificity of each agar and bacteria
import cv2
import numpy as np
from CLED_program.HistogramWriting import CLED_image
from skimage.filters import try_all_threshold
import matplotlib.pyplot as plt

#first agar: MRSA
def MRSA(image):
    #transform the image to hsv and extract the saturation.
    _,sat,_ = cv2.split(cv2.cvtColor(image, cv2.COLOR_BGR2HSV))
    #invert white with black, highlighting colonies with a dark color
    sat = 255 - sat
    #background removal
    kSize = 75
    blur = cv2.GaussianBlur(sat, (kSize, kSize), 0)
    mean_blur = np.mean(blur)
    corr_img = sat - blur + np.uint8(mean_blur)

    #apply a binary threshold and otsu to further highlight colonies.
    _, img = cv2.threshold(corr_img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    return img

#second agar: CLED
def CLED(image):
    #function that modifies the image by removing the writing after it is detected and then inserts the colonies detected by the Hough transform
    image = CLED_image(image)
    #transform image to grayscale.
    image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    #I apply the background subtraction
    kSize = 75
    blur = cv2.GaussianBlur(image, (kSize, kSize), 0)
    mean_blur = np.mean(blur)
    corr_img = image - blur + np.uint8(mean_blur)

    #apply a binary threshold and otsu to further highlight colonies.
    _, img = cv2.threshold(corr_img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    return img

#third agar: chocv
def CHOCV(image):

    #find the saturated image
    _,sat,_ = cv2.split(cv2.cvtColor(image, cv2.COLOR_BGR2HSV))

    #I apply background subtraction
    kSize = 75
    blur = cv2.GaussianBlur(sat, (kSize, kSize), 0)
    mean_blur = np.mean(blur)
    corr_img = sat - blur + np.uint8(mean_blur)

    #I apply a filter and binary threshold+otsu to further highlight colonies.
    corr_img = cv2.bilateralFilter(corr_img, 9, 75, 75)
    _, img = cv2.threshold(corr_img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    return img

#fourth agar: CNA
def CNA(image):

    #I find the saturated image
    _,sat,_ = cv2.split(cv2.cvtColor(image, cv2.COLOR_BGR2HSV))

    #I apply background subtraction
    kSize = 75
    blur = cv2.GaussianBlur(sat, (kSize, kSize), 0)
    mean_blur = np.mean(blur)
    corr_img = sat - blur + np.uint8(mean_blur)
    
    #I apply a filter and binary threshold+otsu to further highlight colonies.
    blur = cv2.GaussianBlur(corr_img, (5, 5), 0)
    _, img = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    return img

#fifth agar: CPSE (saturation is not enough since not all colonies have equal color.
#you introduce HUE which works for images where saturation fails)

def CPSE(image):
    #extract saturation and hue images after converting the image from rgb to hsv
    hue,sat,_ = cv2.split(cv2.cvtColor(image, cv2.COLOR_BGR2HSV))
    #apply a threshold to the saturation to see if the latter works (if it doesn't then the image will be mostly black)
    thresh = cv2.inRange(sat, 90, 255)

    #count the non-black pixels, if they are of a number less than 20000 then we are dealing with an image that needs HUE.
    if cv2.countNonZero(thresh) < 20000:
        #invert black with white to highlight colonies.
        hue = 255 - hue

        #check
        #print('1')

        #background subtraction
        kSize = 75
        blur = cv2.GaussianBlur(hue, (kSize, kSize), 0)
        mean_blur = np.mean(blur)
        corr_img = hue - blur + np.uint8(mean_blur)

        #I apply a filter and binary threshold+otsu to further highlight colonies.
        blur = cv2.GaussianBlur(corr_img, (5, 5), 0)
        _, img = cv2.threshold(blur,225,255,cv2.THRESH_BINARY)

    #otherwise if the image is mostly white.
    else:
        #invert white with black
        sat = 255 - sat

        #background subtraction
        kSize = 75
        blur = cv2.GaussianBlur(sat, (kSize, kSize), 0)
        mean_blur = np.mean(blur)
        corr_img = sat - blur + np.uint8(mean_blur)

        #I apply a filter and binary threshold+otsu to further highlight colonies.
        blur = cv2.GaussianBlur(corr_img, (5, 5), 0)
        _, img = cv2.threshold(blur,172,255,cv2.THRESH_BINARY)
        #check
        #print('2')

    return img

#sesto agar: MCK
def MCK(image):

    #I find the saturated image
    _,sat,_ = cv2.split(cv2.cvtColor(image, cv2.COLOR_BGR2HSV))

    #invert white with black
    sat = 255 - sat
    
    #applico un filtro e una threshold binario e otsu per evidenziare ulteriormente le colonie
    blur = cv2.GaussianBlur(sat, (5, 5), 0)
    
    _, img = cv2.threshold(blur,109,255,cv2.THRESH_BINARY)
    return img
