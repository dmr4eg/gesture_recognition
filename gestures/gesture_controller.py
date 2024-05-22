import threading
from gestures.video_capture_manager import VideoCaptureManager
from gestures.frame_processor import FrameProcessor
from gestures.gesture_recognizer import GestureRecognizer
from gestures.gesture_callback_manager import GestureCallbackManager
from gestures.thread_pool_manager import ThreadPoolManager
from spotipy import Spotify
from spotipy.oauth2 import SpotifyOAuth

class GestureController: 
    def __init__(self, gesture_callback):
        """
        Initialize the GestureController with the necessary components.
        
        :param gesture_callback: The callback function to handle gestures.
        """
        # Set up the Spotify client with OAuth authentication
        self.spotify_client = Spotify(auth_manager=SpotifyOAuth(
            client_id=os.getenv("SPOTIPY_CLIENT_ID"),
            client_secret=os.getenv("SPOTIPY_CLIENT_SECRET"),
            redirect_uri=os.getenv("SPOTIPY_REDIRECT_URI"),
            scope="user-modify-playback-state,user-read-playback-state"
        ))
        
        # Initialize the GestureCallbackManager
        self.gesture_callback_manager = GestureCallbackManager(
            gesture_callback, self.spotify_client, delay=2
        )

        # Initialize the components for video capture and gesture recognition
        self.video_capture_manager = VideoCaptureManager()
        self.gesture_recognizer = GestureRecognizer()
        self.frame_processor = FrameProcessor(
            self.gesture_recognizer.recognizer,
            self.gesture_recognizer.mp_hands,
            self.gesture_recognizer.mp_drawing,
            self.gesture_recognizer.mp_drawing_styles
        )
        self.thread_pool_manager = ThreadPoolManager()
        self.running = False
        self.thread = None
        self.processed_frames = {}

    def start(self):
        """
        Start the gesture controller by beginning video capture and processing.
        """
        self.running = True
        self.thread = threading.Thread(target=self._run_video_capture)
        self.thread.start()

    def stop(self):
        """
        Stop the gesture controller by stopping video capture and processing.
        """
        self.running = False
        if self.thread:
            self.thread.join()
        self.thread_pool_manager.close()
        self.video_capture_manager.release()

    def _run_video_capture(self):
        """
        Continuously capture video frames and process them for gesture recognition.
        """
        try:
            while self.running:
                ret, frame = self.video_capture_manager.read_frame()
                if not ret:
                    continue

                frame_count = self.video_capture_manager.get_frame_count()
                fps = self.video_capture_manager.get_fps()
                self.thread_pool_manager.submit_frame_for_processing(
                    self.frame_processor.process_frame, (frame, frame_count, fps)
                )

                processed_result = self.thread_pool_manager.retrieve_processed_frames()
                if processed_result:
                    processed_frame, gesture_name = processed_result
                    self.processed_frames["frame"] = processed_frame
                    if gesture_name:
                        self.gesture_callback_manager.call_callback_based_on_gesture(
                            gesture_name
                        )
        finally:
            self.video_capture_manager.release()

    def get_latest_processed_frame(self):
        """
        Retrieve the latest processed frame.
        
        :return: The latest processed frame if available, otherwise None.
        """
        return self.processed_frames.pop("frame", None)