"""
Histogram Computation of an Image
"""
import cv2 as opencv
import matplotlib.pyplot as plt

image = opencv.imread('images/beautiful-water-drop-on-dandelion-260nw-789676552.jpg')
opencv.imshow('Test Image',image)
opencv.waitKey(0)

gray_image = opencv.cvtColor(image,opencv.COLOR_BGR2GRAY)
opencv.imshow('Grayscale of Image',gray_image)
opencv.waitKey(0)


### Grayscale Histogram Computation of the Image
gray_hist = opencv.calcHist([gray_image],[0],None, [256],[0,256])
plt.figure()
plt.title('Grayscale histogram')
plt.xlabel('Pixel Bins')
plt.ylabel('No of Pixels')
plt.xlim([0,256])
plt.plot(gray_hist)
plt.show()

#### Color Histogram Computation of the Image
colors = ('b','g','r')

for i,col in enumerate(colors):
    hist = opencv.calcHist([image],[i],None,[256],[0,256])
    plt.plot(hist,color=col)
    plt.xlim([0,256])
plt.title('Color Histogram')
plt.xlabel('Pixel Bins')
plt.ylabel('No of Labels')
plt.show()
