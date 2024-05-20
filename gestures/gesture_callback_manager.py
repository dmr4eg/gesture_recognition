class GestureCallbackManager:
    def __init__(self, gesture_callback):
        self.gesture_callback = gesture_callback

    def call_callback_based_on_gesture(self, gesture_name):
        gesture_name = gesture_name.lower()
        if gesture_name == "thumb_up":
            self.gesture_callback("scroll_up")
        elif gesture_name == "thumb_down":
            self.gesture_callback("scroll_down")
