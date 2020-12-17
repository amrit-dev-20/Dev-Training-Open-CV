import cv2

path ='images/beautiful-water-drop-on-dandelion-260nw-789676552.jpg'
window_name = "Test Window to Display Images"
image = cv2.imread(path)
cv2.imshow(window_name,image)
cv2.waitKey(0)
cv2.destroyAllWindows()


