import numpy as np
import cv2

#function that needs to find colonies, I pass the image and the mask that contains the rectangle
def GetColonies(image,mask):

    #convert image to grayscale
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    #I isolate the image contained in the rectangle
    writing_gray = cv2.bitwise_and(image_gray, image_gray, mask=mask)

    #I identify the circles present in the rectangular mask with the Hough transform 
    circles = cv2.HoughCircles(writing_gray,cv2.HOUGH_GRADIENT,1,12,param1=45,param2=13,minRadius=4,maxRadius=15)

    circles = np.uint16(np.around(circles))
    
    for i in circles[0,:]:
        # draw the outer circle
        cv2.circle(writing_gray,(i[0],i[1]),i[2],(0,255,0),2)

    return circles
