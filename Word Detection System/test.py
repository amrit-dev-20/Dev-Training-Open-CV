"""
This program is to detect words in a given documentation image 
"""

import cv2
import os
import numpy as np
from matplotlib import pyplot as plt

# To Read an Image from a specific File
img = cv2.imread('images/Appointment-Letter-Format-in-Word.jpg',cv2.IMREAD_UNCHANGED)
height = img.shape[0]
width = img.shape[1]
channels = img.shape[2] 
cv2.imshow("Test Image",img)
cv2.waitKey(0)

#Coverting Image to Binary and then performing Otsu Thresholding 
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
(threshold,img_black_white) = cv2.threshold(img_gray,127,255,cv2.THRESH_OTSU+cv2.THRESH_BINARY)
cv2.imshow("Black and White Image",img_black_white)
cv2.waitKey(0)

height, width = img_black_white.shape

for i in range(0,height):
    for j in range(0, width):
        if img_black_white[i,j]==255:
            img_black_white[i,j]=0
        else:
            img_black_white[i,j]=1

print(img_black_white)

row_sum = []

#row_image = []
for i in range(0,height):
    sum=0
    for j in range(0,width):
        sum+=int(img_black_white[i,j])
    row_sum.append(sum)

line_beginning = []
line_endings = []

for i in range(1,len(row_sum)):
    if(row_sum[i-1]==0 and row_sum[i]!=0):
        line_beginning.append(i)
    elif(row_sum[i-1]!=0 and row_sum[i]==0):
        line_endings.append(i)


directory ="images/solution"
os.chdir(directory)

print(line_beginning)
print(line_endings)
cv2.imshow("Test",img[49:59,:])
cv2.waitKey(0)

for i in range(0,len(line_beginning)):
    x=line_beginning[i]
    x2=line_endings[i]
    img_slice = img_black_white[x:x2,:]
    column_sum_slice = img_slice.sum(axis = 0)
    print(column_sum_slice)
    column_slice_beginning = []
    column_slice_endings = []
    for j in range(1,len(column_sum_slice)):
        if(column_sum_slice[j-1]==0 and column_sum_slice[j]!=0):
            column_slice_beginning.append(j)
        elif(column_sum_slice[j-1]!=0 and column_sum_slice[j]==0):
            column_slice_endings.append(j)
    print(column_slice_beginning)
    print(column_slice_endings)
    for r in range(0,len(column_slice_beginning)):
        filename=str(i)+str(r)+'.jpg'
        cv2.imshow("Result",img[x:x2,column_slice_beginning[r]:column_slice_endings[r]])
        cv2.waitKey(0)
        cv2.imwrite(filename,img[x:x2,column_slice_beginning[r]:column_slice_endings[r]])



cv2.destroyAllWindows()

            







