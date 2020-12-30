"""
The following code is to convert multiple images to grayscale.
"""


import glob
import cv2 as opencv
import time
import argparse
from os import listdir, makedirs


def my_timer(original_func):
    """
    - A decorator for convert_to_grayscale() function.
    - This decorator calculates the time take to convert single & all images.
    """
    def wrapper(*args, **kwargs):
        image_count = len(listdir(input_path))
        start_time = time.time()
        time.sleep(1)
        result = original_func(*args, **kwargs)
        end_time = time.time()
        duration = end_time-start_time
        dur_per_image = duration/image_count
        print('{}() ran in: {}secs'.format(original_func.__name__, duration))
        print('Time Taken to Convert Single Image: {}'.format(dur_per_image))
        return result
    return wrapper


@my_timer
def convert_to_grayscale(input_path, output_path):
    """
    Steps Involved:
    1. Entering Input and Output Path
    2. Checking whether the Path is same.
    3. Extracting the no of Images and their filenames.(Recursively)
    4. Conversion from BGR TO GRAY scale using openCV
    5. Creation of new images with their curresponding Output Path.
    """
    # Try block to check whether the output path exists.
    try:
        makedirs(output_path)
    except Exception:
        print(" Output Path exists, images will be written in same folder.")
        output_path = input_path
    # List of file Names
    image_list = listdir(input_path)
    input_path = input_path + '/**jpeg'
    # Recursive Parsing of Images
    image_files = glob.glob(input_path, recursive=True)
    count = 0
    for image in image_files:
        image_bgr = opencv.imread(image)
        image_gray = opencv.cvtColor(image_bgr, opencv.COLOR_BGR2GRAY)
        output_image_path = output_path + '/' + str(image_list[count])
        opencv.imwrite(output_image_path, image_gray)
        count += 1


def main(input_path, output_path):
    convert_to_grayscale(input_path, output_path)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', help='Enter Input', type=str, required=True)
    parser.add_argument('--output', help='Enter Output', type=str)
    args = parser.parse_args()
    if args.output is None:
        output_path = args.input
    else:
        output_path = args.output

    input_path = args.input
    main(input_path, output_path)
