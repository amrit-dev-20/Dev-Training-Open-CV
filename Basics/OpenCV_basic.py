"""
This code is responsible for reading an image from a specified folder.
"""

import cv2

# To Read an Image from a specific File
img = cv2.imread('images/beautiful-water-drop-on-dandelion-260nw-789676552.jpg',0)
cv2.imshow("Test Image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

