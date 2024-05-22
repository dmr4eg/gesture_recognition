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
        super().__init__()
        self.paned_window = PanedWindow(self, orient=tk.HORIZONTAL,
                                        sashwidth=5)
        self.paned_window.grid(row=0, column=0, sticky="nsew")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.gesture_controller = GestureController(self.handle_gesture)

        self.protocol("WM_DELETE_WINDOW", self.destroy)

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
        print("Destroying Gesture Recongiton...")
        self.gesture_controller.stop()
        super().destroy()