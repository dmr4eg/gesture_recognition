# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set environment variables to avoid interactive prompts during package installations
ENV DEBIAN_FRONTEND=noninteractive

# Set the working directory in the container
WORKDIR /usr/src/app

# Install tkinter, xvfb, supervisord, and other dependencies
RUN apt-get update && apt-get install -y \
    python3-tk \
    xvfb \
    supervisor \
    libglib2.0-0 \
    libgl1-mesa-glx \
    libxrender1 \
    libxrandr2 \
    libfontconfig1 \
    && apt-get clean

# Copy the current directory contents into the container at /usr/src/app
COPY . .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the supervisord.conf to the container
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

# Expose the Flask port
EXPOSE 5000

# Define environment variables
ENV SPOTIPY_CLIENT_ID=<6adf5dcb7d494b25919a562e5876d48c>
ENV SPOTIPY_CLIENT_SECRET=<abca7dbdbae446e88b6d24e0b83284f5>
ENV SPOTIPY_REDIRECT_URI=<http://localhost:8888/callback>

# Run supervisord
CMD ["supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]