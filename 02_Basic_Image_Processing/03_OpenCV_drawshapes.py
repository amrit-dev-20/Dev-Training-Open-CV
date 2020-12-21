"""
Drawing Shapes and coloring in this code
"""
import cv2 as opencv
import numpy as np

"""
1. Creation of blank image
   - Use numpy to create a blank image.
   - most common datatypes: uint8
"""
blank_image = np.zeros((500,500,3),dtype='uint8')
bl_window = opencv.imshow('Blank Image',blank_image)
opencv.waitKey(0)
opencv.destroyWindow(bl_window)

"""
2. Paint with a specific color(BGR Format)
   - Blue color
   - Green color
   - Red color
"""
#Blue Color
blank_image[:] = 255,0,0
opencv.imshow('Blue Color',blank_image)
opencv.waitKey(0)

#Green color
blank_image[:] = 0,255,0
opencv.imshow('Green Color',blank_image)
opencv.waitKey(0)

#Red color
blank_image[:] = 0,0,255
opencv.imshow('Red Color',blank_image)
opencv.waitKey(0)


#Colouring a specific region
blank_image[:] = 0,0,0
blank_image[200:300,300:400] = 0,255,0
opencv.imshow('Green Rectangle',blank_image)
opencv.waitKey(0)

"""
3. Drawing Shapes on Blank Image using OpenCV
    - Rectangle/Square
    - Circle
    - Line
    - Putting Text
"""

##Drawing Shapes using OpenCV
blank_image[:]=0,0,0
opencv.rectangle(blank_image,(0,0),(250,250),(0,255,0),thickness=opencv.FILLED) 
opencv.imshow('Green Rectangle using OpenCV Function',blank_image)
opencv.waitKey(0)

#Drawing a Circle using OpenCV
blank_image[:]=0,0,0
opencv.circle(blank_image, (250,250),(40),(255,0,0),thickness=3)
opencv.imshow("Blue circle with a radius: 40", blank_image)
opencv.waitKey(0)

#Drawing a Line using OpenCV
blank_image[:]=0,0,0
opencv.line(blank_image,(0,0), (250,250),(0,0,255),thickness=2)
opencv.imshow("Line from 0,0 to 250,250",blank_image)
opencv.waitKey(0)

##Writing a text on a blank Image using OpenCV
blank_image[:] =0,0,0
opencv.putText(blank_image,'Hello World', (0,50), opencv.FONT_HERSHEY_TRIPLEX,1.0,(0,255,0),thickness=1)
opencv.imshow("Text on a Image", blank_image)
opencv.waitKey(0)



#Changing(Resizing) the shape of the rectangle 
blank_image[:]=0,0,0
resized_width = blank_image.shape[1]//4
resized_height = blank_image.shape[0]//4
opencv.rectangle(blank_image,(0,0),(resized_width,resized_height),(0,255,0),thickness=opencv.FILLED) 
opencv.imshow(' Resized Green Rectangle',blank_image)
opencv.waitKey(0)


opencv.destroyAllWindows()
