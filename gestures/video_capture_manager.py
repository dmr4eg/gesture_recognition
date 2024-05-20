import cv2 as cv


class VideoCaptureManager:
    def __init__(self):
        self._cap = cv.VideoCapture(0)
        self._frame_count = 0

    def read_frame(self):
        ret, frame = self._cap.read()
        if ret:
            self.increment_frame_count()
        return ret, frame

    def get_fps(self):
        return self._cap.get(cv.CAP_PROP_FPS)

    def release(self):
        self._cap.release()

    def increment_frame_count(self):
        self._frame_count += 1

    def decrement_frame_count(self):
        if self._frame_count > 0:
            self._frame_count -= 1

    def get_frame_count(self):
        return self._frame_count
