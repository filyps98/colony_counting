import cv2
import numpy as np
import os
import glob
from AgarReady import MRSA,CLED,CHOCV,CNA,CPSE,MCK

def Choosing_option():
    #choose the type of agar
    print("Type the agar you are using: (if you want to exit write exit)")
    #print("1) mrsa from: 61 to 69  \n2) cled from: 11 to 24  \n3) chocv from: 21 to 37 \n4) cna from: 37 to 45\n5) cpse from: 1 to 18 \n6) mck from: 31 to 39 \n \n")

    #digita sul prompt
    selection = input()
    image = None

    #either you exit, or select the a certain image
    if selection != 'exit':
        print("Insert the number of the image you want to access:")
        number = input()
        image = cv2.imread('__pathImages__/'+str(selection)+'/'+number+'.bmp')

    #I return the name and the image
    return selection, image

#I isolate the disk without the presence of the background
def crop_image(image1):
    #I transform the image in greyscale and I apply blur
    img = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
    img = cv2.medianBlur(img,5)

    #I identify the circles
    circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,2,10000,minRadius=900,maxRadius=950)
    circles = np.uint16(np.around(circles))

    #I create a mask and I draw the found circles
    height,width = img.shape
    mask = np.zeros((height,width), np.uint8)
    circle_img = cv2.circle(mask,(circles[0][0][0],circles[0][0][1]),circles[0][0][2]-200,255,thickness=-1)

    #I obtain only the disk with black background
    masked_data = cv2.bitwise_and(image1, image1, mask=circle_img)

    #I identify the disk contour and I cut the square that contains it
    gray = cv2.cvtColor(masked_data, cv2.COLOR_BGR2GRAY)
    _,thresh = cv2.threshold(gray,1,255 ,cv2.THRESH_BINARY)
    contours,_ = cv2.findContours(thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    x,y,w,h = cv2.boundingRect(contours[0])
    crop = masked_data[y: y+h, x: x+w]

    #the crop becomes white
    crop[np.where(crop == 0)] = 255
    return crop

def main():
    
    #Cycle that calls the specific function that processes the image and returns an image that highlights the colonies 
    while True:
        choice, image = Choosing_option()

        if choice == 'mrsa':
            image = crop_image(image)
            cv2.imwrite('__result__',MRSA(image))
        elif choice == 'cled':
            image = crop_image(image)
            cv2.imwrite('__result__',CLED(image))
        elif choice == 'chocv':
            image = crop_image(image)
            cv2.imwrite('__result__',CHOCV(image))
        elif choice == 'cna':
            image = crop_image(image)
            cv2.imwrite('__result__',CNA(image))
        elif choice == 'cpse':
            image = crop_image(image)
            cv2.imwrite('__result__',CPSE(image))
        elif choice == 'mck':
            image = crop_image(image)
            cv2.imwrite('__result__',MCK(image))
        elif choice == 'exit':
            break





if __name__ == "__main__":
    main()
