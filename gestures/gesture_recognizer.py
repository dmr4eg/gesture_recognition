import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision

class GestureRecognizer:
    def __init__(self):
        """
        Initialize the GestureRecognizer by setting up MediaPipe components and creating the gesture recognizer.
        """
        self._initialize_mediapipe_components()
        self.recognizer = self._create_gesture_recognizer()

    def _initialize_mediapipe_components(self):
        """
        Initialize the necessary MediaPipe components for hand detection and drawing utilities.
        """
        self.mp_hands = mp.solutions.hands  # Initialize MediaPipe Hands solution
        self.mp_drawing = mp.solutions.drawing_utils  # Initialize drawing utilities
        self.mp_drawing_styles = mp.solutions.drawing_styles  # Initialize drawing styles

    def _create_gesture_recognizer(self):
        """
        Create the gesture recognizer using MediaPipe's vision API with specified options.
        
        :return: An instance of MediaPipe's GestureRecognizer.
        """
        base_options = python.BaseOptions(
            model_asset_path='gesture_recognizer.task')  # Set the path to the gesture recognizer model
        options = vision.GestureRecognizerOptions(
            base_options=base_options, running_mode=vision.RunningMode.VIDEO)  # Set options for video mode
        return vision.GestureRecognizer.create_from_options(options)  # Create and return the gesture recognizer
