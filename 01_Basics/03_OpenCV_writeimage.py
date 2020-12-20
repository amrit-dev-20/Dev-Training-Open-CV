import cv2
import os

image_path = 'images/beautiful-water-drop-on-dandelion-260nw-789676552.jpg'
directory = 'images'
image = cv2.imread(image_path)

os.chdir(directory)

filename = 'save_image_1.jpg'
cv2.imwrite(filename,image)
new_file_path = str(filename)
image_2 = cv2.imread(new_file_path,0)
cv2.imshow("Written Image Showed",image_2)
cv2.waitKey(0)
cv2.destroyAllWindows()


