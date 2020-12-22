"""
Arithmetic Operations like Addition, Subtraction, and Bitwise Operations(AND, OR, NOT, XOR) 
can be applied to the input images. These operations can be helpful in enhancing the 
properties of the input images. 

The Image arithmetics are important for analyzing the input image properties.
"""

import cv2 as cv
import numpy as np

img1 = cv.imread('images/beautiful-water-drop-on-dandelion-260nw-789676552.jpg')
img2 = cv.imread('images/car.jpeg')
print(img1.shape)

## Addition of an Image
weightedSum = cv.addWeighted(img1, 0.5, img2, 0.4, 0) 
cv.imshow("Image 1",img1)
cv.waitKey(0)
cv.imshow("Image 2",img2)
cv.waitKey(0)
cv.imshow('Weighted Image', weightedSum)
if cv.waitKey(0) & 0xff == 27:  
    cv.destroyAllWindows()  