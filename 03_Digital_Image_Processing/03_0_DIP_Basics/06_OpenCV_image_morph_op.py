"""
Morphological Operations on Images:

    Morphological operations are used to extract image components that are useful in the representation 
and description of region shape. 

    Morphological operations are some basic tasks dependent on the picture shape. It is typically performed 
on binary images. It needs two data sources, one is the input image, the second one is called structuring 
component. 
    
    Morphological operators take an input image and a structuring component as input and these elements 
are then combines using the set operators. The objects in the input image are processed depending on 
attributes of the shape of the image, which are encoded in the structuring component.
"""
import cv2 as opencv
import numpy as np

### 1. Opening(Erosion and then Dilation)
"""
Opening Operation:
    Opening is similar to erosion as it tends to remove the bright foreground pixels from the edges of 
regions of foreground pixels. The impact of the operator is to safeguard foreground region that has 
similarity with the structuring component, or that can totally contain the structuring component while 
taking out every single other area of foreground pixels. Opening operation is used for removing internal 
noise in an image.
"""
 
 #Reading of Image
image = opencv.imread('images/beautiful-water-drop-on-dandelion-260nw-789676552.jpg')
image_hsv = opencv.cvtColor(image,opencv.COLOR_BGR2HSV)
opencv.imshow('Test Image', image)
opencv.waitKey(0) 
 #defining the mask of the blue range
blue_1 = np.array([110,50,50])
blue_2 = np.array([130,255,255])

 #initializing the mask to be convoluted
mask = opencv.inRange(image_hsv,blue_1,blue_2)

# passing the bitwise_and over 
# each pixel convoluted
result = opencv.bitwise_and(image,image,mask=mask) 

kernel = np.ones((5,5),np.uint8)     
image_opening_morph = opencv.morphologyEx(mask,opencv.MORPH_OPEN,kernel)

opencv.imshow('Mask',mask)
opencv.waitKey(0)

opencv.imshow('Opening',image_opening_morph)
opencv.waitKey(0)


 
### 2. Closing(Dilation and then Erosion)#############
"""
Closing Operation:
    Closing is similar to the opening operation. In closing operation, the 
basic premise is that the closing is opening performed in reverse. It is 
defined simply as a dilation followed by an erosion using the same structuring 
element used in the opening operation.

"""
image_closing_morph = opencv.morphologyEx(mask,opencv.MORPH_CLOSE,kernel)
opencv.imshow('Closing',image_closing_morph)
opencv.waitKey(0) 

opencv.destroyAllWindows()


### 3. Gradient Operation

