"""
The following code is to convert multiple images to grayscale.
"""

import glob
import cv2 as opencv
import time
import argparse
import shutil
import os


def my_timer(original_func):
    """
    - A decorator for convert_to_grayscale() function.
    - This decorator calculates the time take to convert single & all images.
    """
    def wrapper(*args, **kwargs):
        image_count = len(os.listdir(args[0]))
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


def relative_path_extractor(input_path):
    dirname, filename = os.path.split(os.path.abspath(input_path))
    relative_path = os.path.relpath(input_path, start=os.curdir)
    relative_path = relative_path.strip('../')
    relative_path = relative_path.replace(filename, '')
    return relative_path


def file_name_ext_extractor(input_path):
    file_name, ext = os.path.splitext(input_path)
    file_name = os.path.basename(input_path)
    file_name = file_name.split(ext)
    return file_name[0], ext


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
        os.makedirs(output_path)
    except Exception:
        print(" Output Path exists, images will be written in same folder.")
        shutil.rmtree(output_path)
    input_path_ext = '{}{}'.format(input_path, '/**/*')
    # Extension List
    extensions = ('.jpeg', '.jpg', '.png')
    # Recursive Parsing of Images
    for i in extensions:
        img_files = glob.glob('{}{}'.format(input_path_ext, i), recursive=True)
        for image in img_files:
            try:
                # Finding the filename and its Extension
                filename, ext = file_name_ext_extractor(image)
                # Finding the Relative Path
                relative_path = relative_path_extractor(image)
                # Creating the sub directory structure
                output_image_path = os.path.join(output_path, relative_path)
                os.makedirs(output_image_path)
            except Exception:
                print("Path is Same")
            image_bgr = opencv.imread(image)
            # Image Conversion from Color to Grayscale
            image_gray = opencv.cvtColor(image_bgr, opencv.COLOR_BGR2GRAY)
            # Final Image Path
            final_path = '{}/{}{}'.format(output_image_path, filename, ext)
            # Writing of Image in the given Final Path
            opencv.imwrite(final_path, image_gray)


def main(args):
    if args.output is None:
        output_path = args.input
    else:
        output_path = args.output
    input_path = args.input
    convert_to_grayscale(input_path, output_path)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', help='Enter Input', type=str, required=True)
    parser.add_argument('--output', help='Enter Output', type=str)
    args = parser.parse_args()
    main(args)
