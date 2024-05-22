import os
import time
import threading

class GestureCallbackManager:
    def __init__(self, gesture_callback, delay=2):
        self.gesture_callback = gesture_callback
        self.delay = delay
        self.lock = threading.Lock()
        self.last_action_time = time.time()

    def call_callback_based_on_gesture(self, gesture_name):
        current_time = time.time()
        if current_time - self.last_action_time < self.delay:
            return

        gesture_name = gesture_name.lower()
        action_performed = False

        with self.lock:
            if gesture_name == "thumb_up":
                self.gesture_callback("volume up")
                os.system("osascript -e 'set volume output volume (output volume of (get volume settings) + 10)'")
                action_performed = True
            elif gesture_name == "thumb_down":
                self.gesture_callback("volume down")
                os.system("osascript -e 'set volume output volume (output volume of (get volume settings) - 10)'")
                action_performed = True
            elif gesture_name == "iloveyou":
                self.gesture_callback("prevoius track")
                os.system("osascript -e 'tell application \"Spotify\" to previous track'")
                action_performed = True
            elif gesture_name == "pointing_up":
                self.gesture_callback("next track")
                os.system("osascript -e 'tell application \"Spotify\" to next track'")
                action_performed = True
            elif gesture_name == "victory":
                self.gesture_callback("play/pause")
                os.system("osascript -e 'tell application \"Spotify\" to playpause'")
                action_performed = True

            if action_performed:
                self.last_action_time = time.time()
                threading.Thread(target=self.add_delay).start()

    def add_delay(self):
        time.sleep(self.delay)