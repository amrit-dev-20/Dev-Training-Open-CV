"""
Identify a specific Color from the image
"""
import cv2 as opencv
import numpy as np
def empty(a):
    pass

## Introduction to Trackbars
opencv.namedWindow('Trackbars')
opencv.resizeWindow('Trackbars',640,240)
opencv.createTrackbar("Hue Min","Trackbars",3,179,empty)
opencv.createTrackbar("Hue Max","Trackbars",179,179,empty)
opencv.createTrackbar("Sat Min","Trackbars",56,255,empty)
opencv.createTrackbar("Sat Max","Trackbars",255,255,empty)
opencv.createTrackbar("Val Min","Trackbars",120,255,empty)
opencv.createTrackbar("Val Max","Trackbars",255,255,empty)

opencv.waitKey(0)



image = opencv.imread('images/lambo.jpeg')
opencv.imshow('Test Image',image)
opencv.waitKey(0)

while True:
    image_hsv = opencv.cvtColor(image,opencv.COLOR_BGR2HSV)
    opencv.imshow("Conversion to HSV",image_hsv)
    h_min =opencv.getTrackbarPos("Hue Min","Trackbars")
    h_max =opencv.getTrackbarPos("Hue Max","Trackbars")
    s_min =opencv.getTrackbarPos("Sat Min","Trackbars")
    s_max =opencv.getTrackbarPos("Sat Max","Trackbars")
    v_min =opencv.getTrackbarPos("Val Min","Trackbars")
    v_max =opencv.getTrackbarPos("Val Max","Trackbars")
    print(h_min,h_max,s_min,s_max,v_min,v_max)
    #Lower and Uppper Boundaries of the HSV Image
    lower =np.array([h_min,s_min,v_min])
    upper = np.array([h_max,s_max,v_max])

    mask = opencv.inRange(image_hsv,lower,upper)
    image_result = opencv.bitwise_and(image,image,mask=mask)
    
    opencv.imshow("Mask",mask)
    opencv.imshow("Image Result",image_result)
    opencv.waitKey(1)
    





opencv.destroyAllWindows()