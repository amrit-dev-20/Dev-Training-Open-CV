"""
This code teaches how to perform basic image transoforamtion using OpenCV
"""
import cv2 as opencv
import numpy as np

image = opencv.imread('images/beautiful-water-drop-on-dandelion-260nw-789676552.jpg')
opencv.imshow('Test Image', image)
opencv.waitKey(0)

"""
Image Transformation consist of the following things:
    - Image Translation
    - Image Rotation
    - Image Resizing (Zooming and shrinking)
    - Image Flipping  


"""
### Image Translation
def translate(iamge, x,y):
    """
    Returns the translated image from the original position to the new position(x,y)
     -x --> moving left  and  x --> moving right
     -y --> moving up and y --> moving down
    """
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (image.shape[1],image.shape[0])
    return opencv.warpAffine(image,transMat,dimensions)

## moving right and moving down(x,y)
translated_right_down = translate(image,50,50)
opencv.imshow('Translation of Image(Right and down)',translated_right_down)
opencv.waitKey(0)

## moving right and moving up
translated_right_up = translate(image,50,-50)
opencv.imshow('Translation of Image(right and up)',translated_right_up)
opencv.waitKey(0)

## moving left and moving down(-x,y)
translated_left_down = translate(image,-50,50)
opencv.imshow('Translation of Image(left and down)',translated_left_down)
opencv.waitKey(0)

## moving left and moving up(-x,y)
translated_left_up = translate(image,-50,-50)
opencv.imshow('Translation of Image(left and up)',translated_left_up)
opencv.waitKey(0)

opencv.destroyAllWindows()
#########################################################################################

### Image Rotation 
def rotate(img, angle, rotPoint = None):
    """
    Returns the  rotated the image based on the angle and rotatuion point
     +ve angle value = counterclockwise
     -ve angle value = clockwise

    """
    (height,width) = img.shape[:2]
    
    if rotPoint is None:
        rotPoint = (width//2,height//2)
    
    rotMat = opencv.getRotationMatrix2D(rotPoint,angle,1.0)
    dimensions = (width,height)

    return opencv.warpAffine(img, rotMat,dimensions)


rotated_counterclockwise = rotate(image, 45)
opencv.imshow('Rotating image Counter-Clockwise',rotated_counterclockwise)
opencv.waitKey(0)

rotated_clockwise = rotate(image, -45)
opencv.imshow('Rotating image Counter-Clockwise',rotated_clockwise)
opencv.waitKey(0)

########################################################################################
#### Other Important Functions

# Resizing of Image(Zooming and Shrinking)


# Flipping the Image
flipped_image = opencv.flip(image,1)
opencv.imshow('Flipped Image',flipped_image)
opencv.waitKey(0)

opencv.destroyAllWindows()


