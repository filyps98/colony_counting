import cv2
import numpy as np
import math

#Algorithm to locate the rectangle that continues the writing, as arguments there are the image and contours found with find contour
def RectRotate(img,cnt):

    #I obtain image shape
    rows, cols = img.shape[:2]
    #find the rectangle that contains the contours
    rect = cv2.minAreaRect(cnt)

    #transform rect in such a way as to change the rectangle, I want it a little wider than what it is now
    rect1 = list(rect[1])
    rect2 = []
    rect1[0] = rect[1][0]+40
    rect1[1] = rect[1][1]+40
    rect2.append(rect[0])
    rect2.append(tuple(rect1))
    rect2.append(rect[2])
    rect2 = tuple(rect2)

    #find the vertices of the rectangle
    box = cv2.boxPoints(rect2)
    box = np.int0(box)
    #transform image to grayscale (useless, but I don't want to touch the instruction because I haven't picked up the program in a while)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    #create a black image the size of the original image
    height,width = img.shape
    mask = np.zeros((height,width), np.uint8)

    #fill in the rectangle of white to form the mask
    cv2.fillPoly(mask,[box],(255,255,255))

    return mask
