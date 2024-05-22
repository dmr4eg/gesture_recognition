import os
import tkinter as tk
from tkinter import PanedWindow
import cv2 as cv
from gestures.gesture_controller import GestureController

def event_arg(func):
    def wrapper(self, _: tk.Event = None):
        return func(self)
    return wrapper

class GestureRecognitionHub(tk.Tk):  
    def __init__(self) -> None:
        # Set DISPLAY environment variable for xvfb
        os.environ['DISPLAY'] = ':99'
        super().__init__()
        self.title("Gesture Recognition Hub")
        self.gesture_controller = GestureController(self.handle_gesture)

    def start_recognition(self):
        self.gesture_controller.start()

    def handle_gesture(self, gesture_command):
        print("Callback received: ", gesture_command)

    def update_cv_window(self):
        processed_frame = self.gesture_controller.get_latest_processed_frame()
        if processed_frame is not None:
            cv.imshow('Gesture Recognition', processed_frame)
        self.after(50, self.update_cv_window)

    def mainloop(self, n=0):
        print("Starting mainloop")
        self.update_cv_window()
        super().mainloop()

    def destroy(self) -> None:
        print("Destroying Gesture Recognition...")
        self.gesture_controller.stop()
        super().destroy()
