import os
import time
import threading
from spotipy import Spotify

class GestureCallbackManager:
    def __init__(self, gesture_callback, spotify_client, delay=2):
        """
        Initialize the GestureCallbackManager with a callback function, Spotify client, and optional delay.
        
        :param gesture_callback: Function to be called based on gesture.
        :param spotify_client: Instance of the Spotify client.
        :param delay: Minimum delay between gesture actions in seconds.
        """
        self.gesture_callback = gesture_callback
        self.spotify_client = spotify_client
        self.delay = delay
        self.lock = threading.Lock()
        self.last_action_time = time.time()

    def call_callback_based_on_gesture(self, gesture_name):
        """
        Call the appropriate callback based on the detected gesture, ensuring a delay between actions.
        
        :param gesture_name: Name of the detected gesture.
        """
        current_time = time.time()
        if current_time - self.last_action_time < self.delay:
            print(f"Gesture {gesture_name} ignored due to delay")
            return

        gesture_name = gesture_name.lower()
        action_performed = False

        with self.lock:
            print(f"Gesture received: {gesture_name}")
            if gesture_name == "thumb_up":
                self.gesture_callback("scroll_up")
                os.system("osascript -e 'set volume output volume (output volume of (get volume settings) + 10)'")
                print("Volume increased")
                action_performed = True
            elif gesture_name == "thumb_down":
                self.gesture_callback("scroll_down")
                os.system("osascript -e 'set volume output volume (output volume of (get volume settings) - 10)'")
                print("Volume decreased")
                action_performed = True
            elif gesture_name == "pointing_up":
                self.gesture_callback("previous_track")
                response = self.spotify_client.previous_track()
                print("Previous Track Response:", response)
                action_performed = True
            elif gesture_name == "iloveyou":
                self.gesture_callback("next_track")
                response = self.spotify_client.next_track()
                print("Next Track Response:", response)
                action_performed = True
            elif gesture_name == "victory":
                self.gesture_callback("play_pause")
                currently_playing = self.spotify_client.current_playback()
                if currently_playing and currently_playing['is_playing']:
                    response = self.spotify_client.pause_playback()
                    print("Pause Playback Response:", response)
                else:
                    response = self.spotify_client.start_playback()
                    print("Start Playback Response:", response)
                action_performed = True

            if action_performed:
                self.last_action_time = time.time()
                threading.Thread(target=self.add_delay).start()
            else:
                print(f"No action performed for gesture: {gesture_name}")

    def add_delay(self):
        """
        Add a delay before the next gesture can be processed.
        """
        time.sleep(self.delay)

def gesture_callback(action):
    """
    Example callback function to handle actions based on gestures.
    
    :param action: Action to be performed based on the gesture.
    """
    print(f"Action: {action}")
