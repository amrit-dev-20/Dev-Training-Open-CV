import cv2 as opencv
import numpy as np

image = opencv.imread('images/beautiful-water-drop-on-dandelion-260nw-789676552.jpg')
opencv.imshow('Test Image', image)
opencv.waitKey(0)

gray_image = opencv.cvtColor(image, opencv.COLOR_BGR2GRAY)
opencv.imshow('Gray Image', gray_image)
opencv.waitKey(0)

### laplacian method of Edge Detection
lap_image = opencv.Laplacian(gray_image,opencv.CV_64F)
lap_image = np.uint8(np.absolute(lap_image))
opencv.imshow('Laplacian Image',lap_image)
opencv.waitKey(0)


### Sobel method of Edge Detection
sobelx_image = opencv.Sobel(gray_image,opencv.CV_64F,1,0)
opencv.imshow('Sobel X Image',sobelx_image)
opencv.waitKey(0)

sobely_image = opencv.Sobel(gray_image,opencv.CV_64F,0,1)
opencv.imshow('Sobel y Image',sobely_image)
opencv.waitKey(0)

combined_sobel = opencv.bitwise_or(sobelx_image,sobely_image)
opencv.imshow('Combined Sobel X and Y Image',combined_sobel)
opencv.waitKey(0)

### Canny Edge Method
canny_edge_image = opencv.Canny(gray_image,125, 175)
opencv.imshow('Canny Edges in Image',canny_edge_image)
opencv.waitKey(0)

