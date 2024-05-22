from collections import deque
from multiprocessing.pool import ThreadPool
import cv2 as cv

class ThreadPoolManager:
    def __init__(self):
        """
        Initialize the ThreadPoolManager with a thread pool and frame queue.
        """
        self.pool = ThreadPool(processes=cv.getNumberOfCPUs())  # Create a thread pool with number of CPU cores
        self.frame_queue = deque()  # Initialize a deque to hold frame processing tasks
        self.max_frames_in_queue = 2  # Set maximum number of frames to keep in the queue

    def submit_frame_for_processing(self, func, args) -> None:
        """
        Submit a frame for processing if the frame queue is not full.
        
        :param func: The function to apply to the frame.
        :param args: The arguments to pass to the function.
        """
        if len(self.frame_queue) < self.max_frames_in_queue:
            task = self.pool.apply_async(func, args)  # Submit the function and arguments to the thread pool
            self.frame_queue.append(task)  # Add the task to the queue

    def retrieve_processed_frames(self) -> tuple:
        """
        Retrieve the processed frames from the queue.
        
        :return: A tuple containing the processed frame and any associated data.
        """
        while self.frame_queue and self.frame_queue[0].ready():  # Check if the first task in the queue is ready
            return self.frame_queue.popleft().get()  # Remove and return the processed frame
        return None, None  # Return None if no frames are ready

    def close(self):
        """
        Close the thread pool and wait for all the tasks to complete.
        """
        self.pool.close()  # Prevent any more tasks from being submitted
        self.pool.join()  # Wait for all the worker threads to exit
