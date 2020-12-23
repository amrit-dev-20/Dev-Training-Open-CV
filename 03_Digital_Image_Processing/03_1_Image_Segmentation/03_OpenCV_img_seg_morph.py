
import cv2 as opencv
import numpy as np 

image = opencv.imread('images/coin-detection.jpeg')
opencv.imshow('Test Image',image)
opencv.waitKey(0)

## Conversion to GrayScale
gray_image = opencv.cvtColor(image, opencv.COLOR_BGR2GRAY)
opencv.imshow('Grayscale Image',gray_image)
opencv.waitKey(0)

## Otsu's Thresholding
threshold_value, thresholded_image = opencv.threshold(gray_image, 0, 255, opencv.THRESH_BINARY_INV + opencv.THRESH_OTSU)
opencv.imshow("Thesholded Image",thresholded_image)
opencv.waitKey(0)

## Noise Removal
#Closing 
kernel = np.ones((3, 3), np.uint8) 
closing = opencv.morphologyEx(thresholded_image, opencv.MORPH_CLOSE, 
                            kernel, iterations = 2) 
  
# Background area using Dialation 
bg = opencv.dilate(closing, kernel, iterations = 1) 

# Finding foreground area 
dist_transform = opencv.distanceTransform(closing, opencv.DIST_L2, 0) 
ret, fg = opencv.threshold(dist_transform, 0.02* dist_transform.max(), 255, 0) 


opencv.imshow('Final result',fg)
opencv.waitKey(0)

opencv.destroyAllWindows(0)

