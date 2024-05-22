import os
import tkinter as tk
from tkinter import PanedWindow
import cv2 as cv
from gestures.gesture_controller import GestureController

def event_arg(func):
    """
    Decorator to pass a default event argument to functions.
    """
    def wrapper(self, _: tk.Event = None):
        return func(self)
    return wrapper

class GestureRecognitionHub(tk.Tk):  
    def __init__(self) -> None:
        """
        Initialize the GestureRecognitionHub application.
        """
        # Set DISPLAY environment variable for xvfb
        os.environ['DISPLAY'] = ':99'
        super().__init__()
        self.title("Gesture Recognition Hub")
        self.gesture_controller = GestureController(self.handle_gesture)
        
        # Optionally, add any UI components here
        # e.g., self.create_ui()

    def start_recognition(self):
        """
        Start the gesture recognition process.
        """
        self.gesture_controller.start()

    def handle_gesture(self, gesture_command):
        """
        Handle the callback for recognized gestures.
        
        :param gesture_command: The command associated with the recognized gesture.
        """
        print("Callback received: ", gesture_command)

    def update_cv_window(self):
        """
        Update the OpenCV window with the latest processed frame.
        """
        processed_frame = self.gesture_controller.get_latest_processed_frame()
        if processed_frame is not None:
            cv.imshow('Gesture Recognition', processed_frame)
        self.after(50, self.update_cv_window)  # Schedule the next update

    def mainloop(self, n=0):
        """
        Start the main loop of the Tkinter application.
        
        :param n: Number of iterations for the main loop (default is 0, which means run indefinitely).
        """
        print("Starting mainloop")
        self.update_cv_window()
        super().mainloop(n)

    def destroy(self) -> None:
        """
        Clean up resources and stop the gesture recognition process before closing the application.
        """
        print("Destroying Gesture Recognition...")
        self.gesture_controller.stop()
        super().destroy()
