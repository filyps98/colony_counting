import numpy as np
import cv2

#algorithm that transfers colonies to the original image
#pass to function all circles found, the original image and the image that underwent inpainting
def Selection_colonies(image,inpainted, circles):

    #transform the image to grayscale and create a mascera
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    height,width = image_gray.shape
    maskdef = np.zeros((height,width), np.uint8)

    #for every circle
    for i in circles[0]:

        #I create a mask
        mask = np.zeros((height,width), np.uint8)
        #I transfer the circles to it
        cv2.circle(mask,(i[0],i[1]),i[2],255,thickness=-1)
        #create an image with the colored colony (the circle just drawn) and black background
        single = cv2.bitwise_and(image, image, mask=mask)

        #to count how many white pixels are in the image.
        sum = cv2.countNonZero(cv2.inRange(cv2.cvtColor(single,cv2.COLOR_BGR2GRAY),255,255))

        #if the ratio of the number of white pixels to the radius of the colony is less than 3
        #then I transfer the single colony (white color now) to the mask declared at the beginning
        if sum/i[2] <= 3:
            cv2.circle(maskdef,(i[0],i[1]),i[2],255,thickness=-1)

    #Where the final mask has white (where colonies are present) the final image is the same as the original image.
    img = inpainted.copy()
    img[np.where(maskdef == 255)] = image[np.where(maskdef == 255)]

    return img
