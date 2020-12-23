"""
Thresholding in Python:
    Thresholding is a technique in OpenCV, which is the assignment of pixel values in relation to 
the threshold value provided. In thresholding, each pixel value is compared with the threshold value. 
If the pixel value is smaller than the threshold, it is set to 0, otherwise, it is set to a maximum 
value (generally 255). 

    There are 3 types of thresholding:
        - Simple Thresholding
        - Adaptive Thesholding
        - Otsu's Thresholding
"""
import cv2 as opencv

image = opencv.imread("images/beautiful-water-drop-on-dandelion-260nw-789676552.jpg",0)
opencv.imshow("Test Image",image)
opencv.waitKey(0)


### Simple Thresholding
"""
    1. Simple Thresholding
    The basic Thresholding technique is Binary Thresholding. For every pixel, the same threshold value is 
applied. If the pixel value is smaller than the threshold, it is set to 0, otherwise, it is set to a 
maximum value.

    Thresholding techniques possible in OpenCV:
            - cv2.THRESH_BINARY: If pixel intensity is greater than the set threshold, value set to 255, 
                                 else set to 0 (black).

            - cv2.THRESH_BINARY_INV: Inverted or Opposite case of cv2.THRESH_BINARY.

            - cv2.THRESH_TRUNC: If pixel intensity value is greater than threshold, it is truncated to the 
                                threshold. The pixel values are set to be the same as the threshold. All 
                                other values remain the same.

            - cv2.THRESH_TOZERO: Pixel intensity is set to 0, for all the pixels intensity, less than the 
                                 threshold value.

            - cv2.THRESH_TOZERO_INV: Inverted or Opposite case of cv2.THRESH_TOZERO.

"""
thresh_bin, thresh_image_bin = opencv.threshold(image, 120,255, opencv.THRESH_BINARY)
thresh_bin_inv, thresh_image_bin_inv = opencv.threshold(image, 120,255, opencv.THRESH_BINARY_INV)
thresh_trunc, thresh_image_trunc = opencv.threshold(image,120,255,opencv.THRESH_TRUNC)
thresh_tozero, thresh_image_tozero = opencv.threshold(image,120,255, opencv.THRESH_TOZERO)
thresh_tozero_inv,thresh_image_tozero_inv = opencv.threshold(image,120,255, opencv.THRESH_TOZERO_INV)

#Result
opencv.imshow("Binary Threshold",thresh_image_bin)
opencv.waitKey(0)
opencv.imshow("Binary Inverse Threshold",thresh_image_bin_inv)
opencv.waitKey(0)
opencv.imshow("Truncated Threshold",thresh_image_trunc)
opencv.waitKey(0)
opencv.imshow("Set to O Threshold",thresh_image_tozero)
opencv.waitKey(0)
opencv.imshow("Seto to 0 Inverse Threshold",thresh_image_tozero_inv)
opencv.waitKey(0)

if opencv.waitKey(0) & 0xff == 27:  
    opencv.destroyAllWindows()  
#####################################################################################


### Adaptive Thresholding
"""
    2. Adaptive Thresholding
    Adaptive thresholding is the method where the threshold value is calculated for smaller regions. 
This leads to different threshold values for different regions with respect to the change in 
lighting. We use cv2.adaptiveThreshold for this.

    There are 2 ways to perform Adaptive Thresholding:
        - Adaptive Thresholding using Mean
        - Adaptive Thresholding using Gaussian
"""
adap_thresh_mean = opencv.adaptiveThreshold(image, 255,opencv.BORDER_CONSTANT ,opencv.ADAPTIVE_THRESH_MEAN_C,199,5)
adap_thresh_gaussian =  opencv.adaptiveThreshold(image, 255,opencv.BORDER_CONSTANT ,opencv.ADAPTIVE_THRESH_GAUSSIAN_C,199,5)


# Result
opencv.imshow("Test Image",image)
opencv.waitKey(0)

opencv.imshow("Adaptive Thresholding using Mean",adap_thresh_mean)
opencv.waitKey(0)

opencv.imshow("Adaptive Thesholding using Gaussian",adap_thresh_gaussian)
opencv.waitKey(0)


if opencv.waitKey(0) & 0xff == 27:  
    opencv.destroyAllWindows()  

#####################################################################################


### Otsu's Thesholding
"""
In Otsu Thresholding, a value of the threshold isn’t chosen but is determined automatically. 
A bimodal image (two distinct image values) is considered. The histogram generated contains 
two peaks. So, a generic condition would be to choose a threshold value that lies in the 
middle of both the histogram peak values.

We use the Traditional cv2.threshold function and use cv2.THRESH_OTSU as an extra flag. 

"""

opencv.imshow("Test Image",image)
opencv.waitKey(0)

thresh_otsu, thresh_image_otsu = opencv.threshold(image, 120, 255, opencv.THRESH_BINARY + opencv.THRESH_OTSU)

opencv.imshow('Otsu Threshold', thresh_image_otsu)
opencv.waitKey(0)

if opencv.waitKey(0) & 0xff == 27:  
    opencv.destroyAllWindows()  
