"""
Bitwise Operations on Images using OpenCV
"""
import cv2 as opencv
import numpy as np

blank_image = np.zeros((400,400),dtype='uint8')

rectangle = opencv.rectangle(blank_image.copy(),(30,30),(370,370),255,-1)
circle = opencv.circle(blank_image.copy(),(200,200), 200, 255, -1)

opencv.imshow("Rectangle",rectangle)
opencv.waitKey(0)

opencv.imshow("Circle",circle)
opencv.waitKey(0)

### bitwise AND --> intersecting regions
bitwise_and = opencv.bitwise_and(rectangle,circle)
opencv.imshow('And Operation of Circle and Rectangle',bitwise_and)
opencv.waitKey(0)

### bitwise OR --> non-intersecting and intersecting regions
bitwise_or = opencv.bitwise_or(rectangle,circle)
opencv.imshow('OR Operation of Circle and Rectangle',bitwise_or)
opencv.waitKey(0)


### bitwise NOT --> Inverse of the image given
bitwise_not = opencv.bitwise_not(circle)
opencv.imshow('NOT Operation of Circle and Rectangle',bitwise_not)
opencv.waitKey(0)


### bitwise XOR  --> non-intersecting regions
bitwise_xor = opencv.bitwise_xor(rectangle,circle)
opencv.imshow('XOR Operation of Circle and Rectangle',bitwise_xor)
opencv.waitKey(0)


opencv.destroyAllWindows()


