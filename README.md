# Gesture Recognition

## Overview

The Gesture Recognition app is a Python-based application that uses computer vision and gesture recognition to control Spotify playback. It integrates OpenCV for video capture, MediaPipe for gesture recognition, and Spotipy for interacting with the Spotify API. Additionally, a Flask web server is provided to handle external gesture commands. After all it is converted into Dockerfile for ease deployment and usage.

## Features

- Real-time gesture recognition using MediaPipe.
- Control Spotify playback (play/pause, next track, previous track, volume up, volume down) using recognized gestures.
- Flask web server to receive gesture commands via HTTP requests.
- Multi-threaded processing to handle video capture and frame processing efficiently.
- Dockerized for easy setup and deployment

## Prerequisites

- Python 3.7+
- OpenCV
- MediaPipe
- Spotipy
- Flask
- Docker

## Installation

1. **Clone the repository:**

```bash
git clone git@gitlab.fel.cvut.cz:assyldam/nsi.git
```

2. **Create a virtual environment and activate it:**

```bash
python3 -m venv venv
source venv/bin/activate
```

3. **Install the required packages:**

```bash
pip install -r requirements.txt
```

4. **Set up the Spotify API:**

- Create a Spotify Developer account and create a new application.
- Add `http://localhost:8080/callback` as a redirect URI in the Spotify Developer Dashboard.
- Copy the client ID and client secret to the `config.py` file.

```bash
export SPOTIPY_CLIENT_ID='your-spotify-client-id'
export SPOTIPY_CLIENT_SECRET='your-spotify-client-secret'
export SPOTIPY_REDIRECT_URI='your-spotify-redirect-uri'
```

## Usage 
1. **Run the application:**

```bash
python main.py
```

or 

```bash
docker build -t gesture-recognition .
docker run -e SPOTIPY_CLIENT_ID='your-spotify-client-id' \
           -e SPOTIPY_CLIENT_SECRET='your-spotify-client-secret' \
           -e SPOTIPY_REDIRECT_URI='your-spotify-redirect-uri' \
           -p 5000:5000 gesture-recognition-hub

```

2. **Send a POST request**
   
```bash
curl -X POST -H "Content-Type: application/json" -d '{"gesture_name": "thumb_up"}' http://localhost:5000/gesture
```

Note: 
If dockerfile is not connecting to a script it is because spotify api has a limit for the number of requests. In that case,for testing application locally, just checkout to commit 731d8cb8703c6d583012e5811cb3cff9df5907b4