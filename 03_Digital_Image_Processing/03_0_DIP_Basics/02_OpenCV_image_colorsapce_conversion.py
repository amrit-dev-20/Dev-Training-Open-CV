"""
Conversion of Color from BGR to Gray and HSV and Vice versa
"""

import cv2 as opencv

image = opencv.imread('images/beautiful-water-drop-on-dandelion-260nw-789676552.jpg')
opencv.imshow("Test Image", image)
opencv.waitKey(0)


#Image Conversion from BGR to GRAY, BGR to HSV, BGR to LAB, BGR to RGB
image_bgr_gray = opencv.cvtColor(image,opencv.COLOR_BGR2GRAY)
opencv.imshow("Conversion from BGR TO GRAY", image_bgr_gray)
opencv.waitKey(0)

image_bgr_hsv =  opencv.cvtColor(image,opencv.COLOR_BGR2HSV)
opencv.imshow("Conversion from BGR TO HSV", image_bgr_hsv)
opencv.waitKey(0)

image_bgr_lab =  opencv.cvtColor(image,opencv.COLOR_BGR2Lab)
opencv.imshow("Conversion from BGR TO Lab", image_bgr_lab)
opencv.waitKey(0)

image_bgr_rgb = opencv.cvtColor(image,opencv.COLOR_BGR2RGB)
opencv.imshow("Conversion from BGR TO RGB", image_bgr_rgb)
opencv.waitKey(0)


###############################################################################
# Reverse Conversions

# Image Conversion from GRAY TO BGR
image_gray_bgr = opencv.cvtColor(image_bgr_gray,opencv.COLOR_GRAY2BGR)
opencv.imshow("Conversion from GRAY TO BGR", image_gray_bgr)
opencv.waitKey(0)

#Image Conversion from HSV TO BGR
image_hsv_bgr = opencv.cvtColor(image_bgr_hsv,opencv.COLOR_HSV2BGR)
opencv.imshow("Conversion from HSV TO BGR", image_hsv_bgr)
opencv.waitKey(0)

#Image Conversion from lab TO BGR
image_lab_bgr = opencv.cvtColor(image_bgr_hsv,opencv.COLOR_Lab2BGR)
opencv.imshow("Conversion from LAB TO BGR", image_lab_bgr)
opencv.waitKey(0)


opencv.destroyAllWindows()