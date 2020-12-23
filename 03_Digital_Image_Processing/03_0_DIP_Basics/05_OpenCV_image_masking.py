"""
Image Masking in OpenCV
"""
import cv2 as opencv
import numpy as np

image = opencv.imread('images/beautiful-water-drop-on-dandelion-260nw-789676552.jpg')
opencv.imshow('Test Image',image)
opencv.waitKey(0)

blank = np.zeros(image.shape[:2],dtype='uint8')
opencv.imshow('Blank Image',blank)
opencv.waitKey(0)

mask = opencv.circle(blank,(image.shape[1]//2+45,image.shape[0]//2+45),100,255,-1)
opencv.imshow('Mask',mask)
opencv.waitKey(0)


masked_image = opencv.bitwise_and(image,image,mask=mask)
opencv.imshow('Masked  Image',masked_image)
opencv.waitKey(0)




opencv.destroyAllWindows()
