#This is the main for editing the image of CLED agars.
import cv2
import numpy as np
from skimage.restoration import inpaint
from CLED_program.RectFindRestore import RectRotate
from skimage.restoration import inpaint
from CLED_program.ExctractColonies import GetColonies
from CLED_program.masktime import Selection_colonies

def CLED_image(image):

    #convert image to grayscale
    grayimage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    #mean and sigma (I use them for threshold boundaries) of the Gaussian describing the writing (P.S: it is not really a Gaussian)
    mean = 76.8831126
    sigma = -3.12580355

    #just the writing with a threshold, everything greater than mean -9*sigma will be white
    ret,thresh1 = cv2.threshold(grayimage,mean - 9*sigma,255 ,cv2.THRESH_BINARY)

    #creating a mask by placing all that is not black white
    thresh1[np.where(thresh1 != 255)] = 0
    #invert mask to highlight writing in black
    mask = 255 - thresh1

    #To this mask I apply findcontours to find contours.
    contours, hierarchy =  cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    #draw outlines on the original image and fill them with white
    cv2.drawContours(image, contours, -1, (255,255,255) , -1)

    #join the different contours found in one array
    con = np.concatenate(contours)

    #individualize a rectangle that contains the writing and return its mask (of this rectangle)
    mask2 = RectRotate(image,con)

    #find the colonies present in the rectangle whose mask I have
    circles = GetColonies(image,mask2)

    #apply a nice inpainting in the original image where the rectangle was before
    dst = cv2.inpaint(image, mask2, 5,cv2.INPAINT_TELEA)
    #apply a blur to even out impainting
    blur = cv2.blur(dst,(50,50),0)
    dst[mask2>0] = blur[mask2>0]

    #colony transfer on the original image
    final = Selection_colonies(image,dst,circles)

    return final
