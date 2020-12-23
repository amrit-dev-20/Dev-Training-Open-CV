"""
Blurring or Smoothing in OpenCV 

"""
import cv2 as opencv


image = opencv.imread('images/beautiful-water-drop-on-dandelion-260nw-789676552.jpg')
opencv.imshow('Test Image',image)
opencv.waitKey(0)

### 1. Averageing Blur
avg_blur_image = opencv.blur(image,(7,7))
opencv.imshow('Image blurred using Average Function',avg_blur_image)
opencv.waitKey(0)


### 2. Gaussian Blur
gaussian_blur_image = opencv.GaussianBlur(image,(7,7),0)
opencv.imshow('Image blurred using the Gaussian Blur',gaussian_blur_image)
opencv.waitKey(0)

### 3. Median Blur
median_blur_image = opencv.medianBlur(image,7)
opencv.imshow('Image blurred using Median Blur',median_blur_image)
opencv.waitKey(0)

### 4. Bilateral Blur
bilateral_blur_image = opencv.bilateralFilter(image, 10, 35, 25)
opencv.imshow('Image blurred using the Bilateral Blur',bilateral_blur_image)
opencv.waitKey(0)





opencv.destroyAllWindows()