"""
This program shows the basic functions implemented in OpenCV
"""

import cv2 as opencv

image = opencv.imread('images/beautiful-water-drop-on-dandelion-260nw-789676552.jpg')
opencv.imshow('Test Image',image)
opencv.waitKey(0)

"""
Basic Functions of OpenCV:
   - Coversion to Grayscle
   - Blurring of Image
   - Edge Cascade(Using Canny Edge Algorithm)
   - Erosion and Dilation
   - Resizing and Cropping of Image
"""

## 1st Function: Conversion of BGR to Grayscale
gray_image =opencv.cvtColor(image,opencv.COLOR_BGR2GRAY)
opencv.imshow('Gray Image',gray_image)
opencv.waitKey(0)

## 2nd Function: Blurring of Image
blur = opencv.GaussianBlur(image,(7,7),opencv.BORDER_DEFAULT)
opencv.imshow('Gaussian Blurred Image', blur)
opencv.waitKey(0)

## 3rd Function: Edge Cascade(Algorithm: Canny Edge Cascade)
canny_edge_image = opencv.Canny(image, 125,175)
opencv.imshow('Edge Cascade using Canny Edge Algorithm',canny_edge_image)
opencv.waitKey(0)

## 4th Function: Dilation of Image 
dilation_image = opencv.dilate(canny_edge_image,(7,7),iterations=3)
opencv.imshow("Dilation of Canny Edge Image", dilation_image)
opencv.waitKey(0)

## 5th Function Erosion of Image
erosion_image = opencv.erode(dilation_image, (3,3),iterations=1)
opencv.imshow('Erosion of the Dilated Image', erosion_image)
opencv.waitKey(0)

## 6th Function: Resizing of Image
resized_image = opencv.resize(image,(500,500), interpolation=opencv.INTER_LINEAR)
opencv.imshow("Resizing Images", resized_image)
opencv.waitKey(0)

## 7th Functions: Cropping of Image
crop_image=resized_image[50:200,200:400]
opencv.imshow('Crop Image', crop_image)
opencv.waitKey(0)
\
opencv.destroyAllWindows()


