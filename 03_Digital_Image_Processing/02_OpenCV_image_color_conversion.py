"""
Conversion of Color from BGR to Gray and HSV and Vice versa
"""

import cv2 as opencv

image = opencv.imread('images/beautiful-water-drop-on-dandelion-260nw-789676552.jpg')
opencv.imshow("Test Image", image)
opencv.waitKey(0)


#Image Conversion from BGR to GRAY and BGR to HSV
image_bgr_gray = opencv.cvtColor(image,opencv.COLOR_BGR2GRAY)
opencv.imshow("Conversion from BGR TO GRAY", image_bgr_gray)
opencv.waitKey(0)

image_bgr_hsv =  opencv.cvtColor(image,opencv.COLOR_BGR2HSV)
opencv.imshow("Conversion from BGR TO HSV", image_bgr_hsv)
opencv.waitKey(0)


#Image Conversion from GRAY TO BGR
image_gray_bgr = opencv.cvtColor(image_bgr_gray,opencv.COLOR_GRAY2BGR)
opencv.imshow("Conversion from GRAY TO BGR", image_gray_bgr)
opencv.waitKey(0)

#Image Conversion from HSV TO BGR
image_hsv_BGR = opencv.cvtColor(image_bgr_hsv,opencv.COLOR_HSV2BGR)
opencv.imshow("Conversion from HSV TO BGR", image_gray_bgr)
opencv.waitKey(0)



opencv.destroyAllWindows()