import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision

class GestureRecognizer:
    def __init__(self):
        self._initialize_mediapipe_components()
        self.recognizer = self._create_gesture_recognizer()

    def _initialize_mediapipe_components(self):
        self.mp_hands = mp.solutions.hands
        self.mp_drawing = mp.solutions.drawing_utils
        self.mp_drawing_styles = mp.solutions.drawing_styles

    def _create_gesture_recognizer(self):
        base_options = python.BaseOptions(
            model_asset_path='gesture_recognizer.task')
        options = vision.GestureRecognizerOptions(
            base_options=base_options, running_mode=vision.RunningMode.VIDEO)
        return vision.GestureRecognizer.create_from_options(options)
