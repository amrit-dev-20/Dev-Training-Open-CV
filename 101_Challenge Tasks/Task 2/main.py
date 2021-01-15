import argparse
import time

import cv2

from helper import resize_image, missing_frames
from helper import convert_to_gray, convert_to_rgb
from video_capture import VideoReader


def main(args):

    start = time.time()

    video_reader = VideoReader(args.video_path)
    frame_counter = 0
    video_reader.start()
    width, height, fps, frame_count = video_reader.get_video_details()
    print(width, height, fps, frame_count)
    time.sleep(0.01)

    while video_reader.more():
        frame_start_time = time.time()
        frame = video_reader.read()
        convert_to_gray(frame)
        convert_to_rgb(frame)
        resize_image(frame)
        frame_duration = time.time() - frame_start_time
        frame_counter += 1
        cv2.imwrite(
            '{}/{}.jpg'.format(args.frames_op_path, frame_counter), frame)
        print('Completed processing frame no: {} in {}(s)'.format(
            frame_counter, frame_duration))
        time.sleep(0.001)

    duration = time.time() - start
    missed_frames = missing_frames(args.frames_op_path, frame_count)

    print('Total time taken: {}'.format(duration))
    print('Total number of frames {}'.format(frame_counter))
    print('Frames per sec: {}'.format(frame_counter/duration))
    print('Frames missed while processing: /n', missed_frames)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--video_path', type=str, required=True)
    parser.add_argument('--frames_op_path', type=str, required=False)
    main(parser.parse_args())
