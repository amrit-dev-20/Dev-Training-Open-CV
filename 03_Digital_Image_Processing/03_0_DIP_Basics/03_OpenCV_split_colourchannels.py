

import cv2


image =  cv2.imread('images/images.png')
B, G, R = cv2.split(image)

#Color Spaces for an Image

cv2.imshow("Original", image)
cv2.waitKey(0)

cv2.imshow("Blue Space", B)
cv2.waitKey(0)

cv2.imshow('Green Space', G)
cv2.waitKey(0)

cv2.imshow('Red Space', R)
cv2.waitKey(0)

merged =cv2.merge([B,G,R])
cv2.imshow('Merged Image',merged)
cv2.waitKey(0)

cv2.destroyAllWindows()

