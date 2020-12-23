"""
    Histogram Equalization in OpenCV
    
    Histogram equalization is a method in image processing of contrast adjustment using 
the image’s histogram.

    This method usually increases the global contrast of many images, especially when the 
usable data of the image is represented by close contrast values. Through this adjustment, 
the intensities can be better distributed on the histogram. This allows for areas of lower 
local contrast to gain a higher  contrast. 

    Histogram equalization accomplishes this by effectively spreading out the most frequent 
intensity values. The method is useful in images with backgrounds and foregrounds that are 
both bright or both dark.

OpenCV has a function to do this, cv2.equalizeHist(). Its input is just grayscale image and 
output is our histogram equalized image.
"""
import cv2 as opencv
import numpy as np

image = opencv.imread("images/beautiful-water-drop-on-dandelion-260nw-789676552.jpg",0)
equ = opencv.equalizeHist(image)

#hstack -> it horizontally stackks the image left to right.
res = np.hstack((image,equ))

opencv.imshow("Image vs. Histogram Equalized Image",res)
opencv.waitKey(0)
opencv.destroyAllWindows()


