"""
Converts all the Images in the path to GrayScale
Steps Involved:
    1. 
"""
import glob
import cv2 as opencv
import time
from os import listdir,makedirs


def convert_to_gray(input_path,output_path):
    try:
        makedirs(output_path)
    except:
        print (" Output Path already exist, images will be written in same folder")
        output_path = input_path
    
    image_list = listdir(input_path)
    input_path = input_path +'/**jpeg'
    image_files = glob.glob(input_path,recursive=True)
    count=0
    for image in image_files:
        image_bgr = opencv.imread(image)
        image_gray =opencv.cvtColor(image_bgr,opencv.COLOR_BGR2GRAY)
        output_image_path = output_path +'/'+str(image_list[count])
        opencv.imwrite(output_image_path,image_gray)
        count+=1

def my_timer(original_func):


def main():
    input_path = input("Please Enter Input Path: ")
    output_path = input("Please Enter Output Path: ")
    image_count = len(listdir(input_path))
    start_time = time.time()
    convert_to_gray(input_path,output_path)
    end_time = time.time()
    duration = end_time-start_time
    print("Time Taken: {}".format(duration))
    print("Conversion Time per Image: {}".format(duration/image_count))


if __name__ == "__main__":
    main()