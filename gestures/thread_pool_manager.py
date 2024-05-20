from collections import deque
from multiprocessing.pool import ThreadPool
import cv2 as cv


class ThreadPoolManager:
    def __init__(self):
        self.pool = ThreadPool(processes=cv.getNumberOfCPUs())
        self.frame_queue = deque()
        self.max_frames_in_queue = 2

    def submit_frame_for_processing(self, func, args) -> None:
        if len(self.frame_queue) < self.max_frames_in_queue:
            task = self.pool.apply_async(func, args)
            self.frame_queue.append(task)

    def retrieve_processed_frames(self) -> tuple:
        while self.frame_queue and self.frame_queue[0].ready():
            return self.frame_queue.popleft().get()
        return None, None

    def close(self):
        self.pool.close()
        self.pool.join()