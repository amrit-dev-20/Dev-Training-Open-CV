"""
This code is responsible for reading a video stream.
"""
import time
from queue import Queue
from threading import Thread
import cv2 as opencv


class VideoReader:
    initialized = False

    def __init__(self, video_path, queue_size=512):
        """
        Initializing the variables 
        """
        self.stream = opencv.VideoCapture(video_path)
        self.q = Queue(maxsize =queue_size)
        self.initialized = True
        self.complete = False
    
    def __read_frames():
        """
        This is a private method, to read the video of the 
        """
        while self.stream.isOpened():

            if not self.q.full():

                frame_captured, frame = self.stream.read()

                if not grabbed:
                    


    
    
    def start_read(self):

        if self.initialized:
            t = Thread(target=self.__read_frames)

