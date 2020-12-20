import cv2 as opencv

video_captured = opencv.VideoCapture('videos/dog.mp4')
def changeRes(width,height):
    #Changeing the size of live video
    video_captured.set(3,wdith)
    video_captured.set(4,height)
