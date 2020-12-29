"""
Shape Detection using OpenCV

"""
import cv2 as opencv
import numpy as np

def getShape(img):
    contours, hierarchy = opencv.findContours(img,opencv.RETR_EXTERNAL,opencv.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = opencv.contourArea(cnt)
        print(area)
        if area >500:
            opencv.drawContours(image_contour,cnt,-1,(255,0,0),3)
            peri = opencv.arcLength(cnt,True)
            # print(peri)
            approx = opencv.approxPolyDP(cnt,0.02*peri,True)
            obj_corner = len(approx)
            x,y,w,h = opencv.boundingRect(approx)
            if(obj_corner==3): 
                object_type = "Triangle"
            elif(obj_corner==4):
                aspRatio = w/float(h)
                if(aspRatio>0.95 and aspRatio<1.05):
                    object_type = "Square"
                else:
                    object_type = "Rectangle"
            elif(obj_corner>4):
                object_type = "Circle"
            opencv.putText(image_contour,object_type,(x+(w//2)-10,y+(h//2)-10),opencv.FONT_HERSHEY_SIMPLEX,0.5,(0,255,0),2)


path = 'images/shapes.jpeg'

image = opencv.imread(path)
image_contour = image.copy()
opencv.imshow('Test Image',image)
opencv.waitKey(0)

gray_image =  opencv.cvtColor(image,opencv.COLOR_BGR2GRAY)
opencv.imshow('Gray Image',gray_image)
opencv.waitKey(0)

blurring_image = opencv.GaussianBlur(gray_image,(7,7),1)
opencv.imshow('Blurred Gray Image',blurring_image)
opencv.waitKey(0)

imgblank = np.zeros(image.shape[:2],dtype='uint8')
opencv.imshow("Blank Image", imgblank)
opencv.waitKey(0)

canny_edge_image = opencv.Canny(blurring_image,50,50)
opencv.imshow('Canny Edge Image',canny_edge_image)
opencv.waitKey(0)
getShape(canny_edge_image)

opencv.imshow('Shapes Identified',image_contour)
opencv.waitKey(0)


opencv.destroyAllWindows()