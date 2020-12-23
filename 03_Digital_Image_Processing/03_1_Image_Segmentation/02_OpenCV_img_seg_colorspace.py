"""
Image Segmentation using Color Spaces
"""

import cv2 as opencv
import numpy as np 

image = opencv.imread('images/beautiful-water-drop-on-dandelion-260nw-789676552.jpg')
opencv.imshow('Test Image',image)
opencv.waitKey(0)

image_hsv = opencv.cvtColor(image,opencv.COLOR_BGR2HSV)
opencv.imshow('Image converted to HSV format',image_hsv)
opencv.waitKey(0)

# Threshold of blue in HSV space 
lower_blue = np.array([35, 140, 60]) 
upper_blue = np.array([255, 255, 180]) 

# preparing the mask to overlay 
mask = opencv.inRange(image_hsv, lower_blue, upper_blue) 

result = opencv.bitwise_and(image,image,mask=mask)
opencv.imshow("Resulted Image",result)
opencv.waitKey(0)

opencv.destroyAllWindows()


