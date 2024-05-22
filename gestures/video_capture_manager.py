import cv2 as cv

class VideoCaptureManager:
    def __init__(self):
        """
        Initialize the VideoCaptureManager, setting up the video capture.
        """
        self._cap = cv.VideoCapture(0)  # Open the default camera (usually the first camera found)
        self._frame_count = 0  # Initialize the frame count

    def read_frame(self):
        """
        Read a frame from the video capture.
        
        :return: A tuple containing a boolean indicating success and the captured frame.
        """
        ret, frame = self._cap.read()  # Read a frame from the video capture
        if ret:
            self.increment_frame_count()  # Increment the frame count if the frame was successfully read
        return ret, frame  # Return the success flag and the frame

    def get_fps(self):
        """
        Get the frames per second (FPS) of the video capture.
        
        :return: The FPS value.
        """
        return self._cap.get(cv.CAP_PROP_FPS)  # Retrieve the FPS from the video capture properties

    def release(self):
        """
        Release the video capture resource.
        """
        self._cap.release()  # Release the video capture object

    def increment_frame_count(self):
        """
        Increment the frame count by one.
        """
        self._frame_count += 1  # Increment the frame count

    def decrement_frame_count(self):
        """
        Decrement the frame count by one, ensuring it doesn't go below zero.
        """
        if self._frame_count > 0:
            self._frame_count -= 1  # Decrement the frame count if it's greater than zero

    def get_frame_count(self):
        """
        Get the current frame count.
        
        :return: The current frame count.
        """
        return self._frame_count  # Return the current frame count
