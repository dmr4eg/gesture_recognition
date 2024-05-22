# app.py

from flask import Flask, request, jsonify
from gestures.gesture_callback_manager import GestureCallbackManager, gesture_callback
from spotipy import Spotify
from spotipy.oauth2 import SpotifyOAuth
import os

app = Flask(__name__)

# Spotify authentication
sp = Spotify(auth_manager=SpotifyOAuth(
    client_id=os.getenv("SPOTIPY_CLIENT_ID"),
    client_secret=os.getenv("SPOTIPY_CLIENT_SECRET"),
    redirect_uri=os.getenv("SPOTIPY_REDIRECT_URI"),
    scope="user-modify-playback-state,user-read-playback-state"
))

# Gesture manager
manager = GestureCallbackManager(gesture_callback, sp, delay=2)

@app.route('/gesture', methods=['POST'])
def gesture():
    data = request.get_json()
    gesture_name = data.get('gesture_name')
    manager.call_callback_based_on_gesture(gesture_name)
    return jsonify({"status": "success", "gesture": gesture_name})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
