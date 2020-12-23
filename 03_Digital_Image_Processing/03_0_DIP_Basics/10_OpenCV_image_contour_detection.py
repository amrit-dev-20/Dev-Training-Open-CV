"""
Contour Detection using OpenCV
"""
import cv2 as opencv
import numpy as np

image = opencv.imread('images/beautiful-water-drop-on-dandelion-260nw-789676552.jpg')
opencv.imshow('Test Image',image)
opencv.waitKey(0)

blank_image = np.zeros(image.shape,dtype='uint8')
opencv.imshow('Blank Image',blank_image)
opencv.waitKey(0)


##Conversion to GrayScale
gray_image = opencv.cvtColor(image,opencv.COLOR_BGR2GRAY)
opencv.imshow('Gray',gray_image)
opencv.waitKey(0)

## Adding Blur
blur = opencv.GaussianBlur(image, (5,5),opencv.BORDER_DEFAULT)
opencv.imshow('Blurred Image(Gaussian)',blur)
opencv.waitKey(0)

### Canny Edge Detection
canny_edge_image = opencv.Canny(blur,125, 175)
opencv.imshow('Canny Edges in Image',canny_edge_image)
opencv.waitKey(0)


### Binary Thresholding
#ret, threshold_image =opencv.threshold(gray_image,125,255,opencv.THRESH_BINARY)
#opencv.imshow("Thresholded Image",threshold_image)
#opencv.waitKey(0)


### Contours creation
"""
Contour Return Options
    RETR_LIST -> returns all the contours of the image
    RETR_TREE -> returns all the contours of the image which follow the hierarchial structure
    RETR_
"""

contours , hierarchy = opencv.findContours(canny_edge_image,opencv.RETR_LIST,opencv.CHAIN_APPROX_SIMPLE)
print(len(contours))

### Drawing contours on a blank Image
opencv.drawContours(blank_image,contours,-1,(255,0,0),1)
opencv.imshow("Contours Drawn",blank_image)
opencv.waitKey(0)










