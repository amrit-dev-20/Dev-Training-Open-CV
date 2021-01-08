import time
import argparse
from video_capture import VideoReader


def main(args):

    start = time.time()

    video_reader = VideoReader(args.video_path)
    video_reader.start()
    time.sleep(0.01)

    while video_reader.more():
        _ = video_reader.read()

        time.sleep(0.001)

    duration = time.time() - start

    print('Total time taken: {}'.format(duration))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--video_path', type=str, required=True)
    parser.add_argment('--output_frame_path',type=str)
    main(parser.parse_args())
