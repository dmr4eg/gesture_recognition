import cv2 as cv  # Import OpenCV library for image processing
import mediapipe as mp  # Import MediaPipe library for machine learning pipelines
from mediapipe.framework.formats import landmark_pb2  # Import protobuf formats for landmarks

class FrameProcessor:
    def __init__(self, recognizer, mp_hands, mp_drawing, mp_drawing_styles):
        """
        Initialize the FrameProcessor with required components.
        
        :param recognizer: The gesture recognizer instance.
        :param mp_hands: MediaPipe hands module.
        :param mp_drawing: MediaPipe drawing utilities.
        :param mp_drawing_styles: MediaPipe drawing styles utilities.
        """
        self.recognizer = recognizer
        self.mp_hands = mp_hands
        self.mp_drawing = mp_drawing
        self.mp_drawing_styles = mp_drawing_styles

    def process_frame(self, frame, frame_count, fps):
        """
        Process a single video frame to detect and annotate hand gestures.
        
        :param frame: The video frame to process.
        :param frame_count: The current frame count in the video.
        :param fps: The frames per second of the video.
        :return: Annotated frame and gesture name if a gesture is recognized.
        """
        frame = cv.flip(frame, 1)  # Flip the frame horizontally
        image_rgb = cv.cvtColor(frame, cv.COLOR_BGR2RGB)  # Convert frame to RGB format
        image_obj = mp.Image(image_format=mp.ImageFormat.SRGB, data=image_rgb)  # Create MediaPipe image object
        timestamp = int(frame_count * 1000 / fps)  # Calculate timestamp in milliseconds
        recognition_result = self.recognizer.recognize_for_video(image_obj, timestamp)  # Recognize gestures
        annotated_image = image_rgb.copy()  # Create a copy of the image for annotation
        return self._annotate_if_gesture(annotated_image, recognition_result, frame)  # Annotate if gesture is detected

    def _annotate_if_gesture(self, image, recognition_result, frame) -> tuple:
        """
        Annotate the image if a gesture is detected.
        
        :param image: The RGB image to annotate.
        :param recognition_result: The result of gesture recognition.
        :param frame: The original frame.
        :return: Annotated image and gesture name if a gesture is detected, otherwise original image and None.
        """
        if recognition_result.gestures:  # Check if any gestures are detected
            return self._annotate_gesture(recognition_result, image, frame)  # Annotate the gesture
        return cv.cvtColor(image, cv.COLOR_RGB2BGR), None  # Convert back to BGR format and return

    def _annotate_gesture(self, recognition_result, annotated_image, frame) -> tuple:
        """
        Annotate the detected gesture on the image.
        
        :param recognition_result: The result of gesture recognition.
        :param annotated_image: The image to annotate.
        :param frame: The original frame.
        :return: Annotated image and detected gesture name.
        """
        top_gesture = recognition_result.gestures[0][0]  # Get the top detected gesture
        gesture_name = top_gesture.category_name  # Get gesture name
        gesture_score = top_gesture.score  # Get gesture confidence score

        for hand_landmarks in recognition_result.hand_landmarks:  # Iterate through detected hand landmarks
            hand_landmarks_proto = landmark_pb2.NormalizedLandmarkList()  # Create protobuf for landmarks
            hand_landmarks_proto.landmark.extend([  # Populate protobuf with landmark data
                landmark_pb2.NormalizedLandmark(
                    x=landmark.x, y=landmark.y, z=landmark.z)
                for landmark in hand_landmarks
            ])

            # Draw hand landmarks on the annotated image
            self.mp_drawing.draw_landmarks(
                annotated_image,
                hand_landmarks_proto,
                self.mp_hands.HAND_CONNECTIONS,
                self.mp_drawing_styles.get_default_hand_landmarks_style(),
                self.mp_drawing_styles.get_default_hand_connections_style()
            )

            # Add text annotation for the gesture name and score
            cv.putText(annotated_image, f"{gesture_name} ({gesture_score:.2f})",
                       (int(hand_landmarks[0].x * frame.shape[1]),
                        int(hand_landmarks[0].y * frame.shape[0])),
                       cv.FONT_HERSHEY_SIMPLEX, 2, (255, 0, 0), 2, cv.LINE_AA)

        return cv.cvtColor(annotated_image, cv.COLOR_RGB2BGR), gesture_name  # Convert back to BGR format and return
