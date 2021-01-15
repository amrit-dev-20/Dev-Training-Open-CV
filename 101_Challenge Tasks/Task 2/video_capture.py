import time
from queue import Queue
from threading import Thread

import cv2


class VideoReader:

    initialized = False

    def __init__(self, video_path, queue_size=1024):
        self.stream = cv2.VideoCapture(video_path)
        self.q = Queue(maxsize=queue_size)
        self.initialized = True
        self.complete = False

    def start(self):

        if self.initialized:
            t = Thread(target=self.__read_frames, args=())
            t.daemon = True
            t.start()

        else:
            raise Exception

    def __read_frames(self):

        while self.stream.isOpened():

            if not self.q.full():

                grabbed, frame = self.stream.read()

                if not grabbed:
                    self.stream.release()
                    self.complete = True
                    return

                self.q.put(frame)

            time.sleep(0.001)

    def get_video_details(self):

        width = int(self.stream.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(self.stream.get(cv2.CAP_PROP_FRAME_HEIGHT))
        fps = self.stream.get(cv2.CAP_PROP_FPS)
        frame_count = int(self.stream.get(cv2.CAP_PROP_FRAME_COUNT))

        return width, height, fps, frame_count

    def more(self):
        return not self.complete

    def read(self):
        return self.q.get()
