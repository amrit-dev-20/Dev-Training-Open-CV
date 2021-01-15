import cv2
import glob
import time


def convert_to_rgb(img):
    time.sleep(0.02)
    return cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


def resize_image(img):
    time.sleep(0.03)
    return cv2.resize(img, (400, 400))


def convert_to_gray(img):
    time.sleep(0.04)
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


def missing_frames(directory, frame_count=80):
    processed_frames = glob.glob(r'{}//*.jpg'.format(directory))
    processed_frames_numbers = []
    for filename in processed_frames:
        file_no_ext = filename.split("/")[-1]
        file_number = file_no_ext.split('.')[-2]
        processed_frames_numbers.append(int(file_number))

    frame_no_list = [x for x in range(1, frame_count+1)]
    return [x for x in frame_no_list if x not in processed_frames_numbers]
