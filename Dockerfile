# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the current directory contents into the container at /usr/src/app
COPY . .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Define environment variables
ENV SPOTIPY_CLIENT_ID=<6adf5dcb7d494b25919a562e5876d48c>
ENV SPOTIPY_CLIENT_SECRET=<abca7dbdbae446e88b6d24e0b83284f5>
ENV SPOTIPY_REDIRECT_URI=<http://localhost:8888/callback>

# Run app.py when the container launches
CMD ["python", "app.py"]


