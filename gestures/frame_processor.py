import cv2 as cv
import mediapipe as mp
from mediapipe.framework.formats import landmark_pb2 


class FrameProcessor:
    def __init__(self, recognizer, mp_hands, mp_drawing, mp_drawing_styles):
        self.recognizer = recognizer
        self.mp_hands = mp_hands
        self.mp_drawing = mp_drawing
        self.mp_drawing_styles = mp_drawing_styles

    def process_frame(self, frame, frame_count, fps):
        frame = cv.flip(frame, 1)
        image_rgb = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
        image_obj = mp.Image(image_format=mp.ImageFormat.SRGB, data=image_rgb)
        timestamp = int(frame_count * 1000 / fps)
        recognition_result = self.recognizer.recognize_for_video(
            image_obj, timestamp)
        annotated_image = image_rgb.copy()
        return self._annotate_if_gesture(annotated_image, recognition_result, frame)

    def _annotate_if_gesture(self, image, recognition_result, frame) -> tuple:
        if recognition_result.gestures:
            return self._annotate_gesture(recognition_result, image, frame)
        return cv.cvtColor(image, cv.COLOR_RGB2BGR), None

    def _annotate_gesture(self, recognition_result, annotated_image, frame) -> tuple:
        top_gesture = recognition_result.gestures[0][0]
        gesture_name = top_gesture.category_name
        gesture_score = top_gesture.score

        for hand_landmarks in recognition_result.hand_landmarks:
            hand_landmarks_proto = landmark_pb2.NormalizedLandmarkList()
            hand_landmarks_proto.landmark.extend([
                landmark_pb2.NormalizedLandmark( 
                    x=landmark.x, y=landmark.y, z=landmark.z)
                for landmark in hand_landmarks
            ])

            self.mp_drawing.draw_landmarks(
                annotated_image,
                hand_landmarks_proto,
                self.mp_hands.HAND_CONNECTIONS,
                self.mp_drawing_styles.get_default_hand_landmarks_style(),
                self.mp_drawing_styles.get_default_hand_connections_style()
            )

            cv.putText(annotated_image, f"{gesture_name} ({gesture_score:.2f})",
                       (int(hand_landmarks[0].x * frame.shape[1]),
                        int(hand_landmarks[0].y * frame.shape[0])),
                       cv.FONT_HERSHEY_SIMPLEX, 2, (255, 0, 0), 2, cv.LINE_AA)

        return cv.cvtColor(annotated_image, cv.COLOR_RGB2BGR), gesture_name