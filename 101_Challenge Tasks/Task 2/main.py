import argparse


def main(args):
    pass


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument('--video_path', type=str, required=True)
    parser.add_argument('--frame_output_path', type=str)
    args = parser.parse_args()
    main(args)
