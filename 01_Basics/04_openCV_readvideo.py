import cv2 as cv

video_captured = cv.VideoCapture('videos/SampleVideo_1280x720_10mb.mp4')
while True:
    isTrue, frame = video_captured.read()
    cv.imshow('Video Displayed', frame)

    if cv.waitKey(20) & 0xFF ==ord('d'):
        break

video_captured.release()
cv.destroyAllWindows()

