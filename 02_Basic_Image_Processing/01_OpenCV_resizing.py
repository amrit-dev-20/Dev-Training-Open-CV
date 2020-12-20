"""
This code is to resize images or videos
"""
import cv2 as opencv

# img = opencv.imread('images/cat_large.jpg')
# opencv.imshow('Cat',img)
# opencv.waitKey(0)

def rescaleFrame(frame, scale=0.25):
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)
    dimensions = (width,height)
    return opencv.resize(frame, dimensions, interpolation=opencv.INTER_AREA)

video_captured = opencv.VideoCapture('videos/dog.mp4')
while True:
    isTrue, frame = video_captured.read()
    frame_resized = rescaleFrame(frame)
    opencv.imshow('Video Displayed', frame)
    opencv.imshow('Frames Resized', frame_resized)

    if opencv.waitKey(20) & 0xFF ==ord('d'):
        break

video_captured.release()
opencv.destroyAllWindows()