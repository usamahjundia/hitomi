# HITOMI

A (knowing me, obviously it's a WIP) surveillance system paired with a web-based dashboard. Possible features are still being brainstormed. This initial version contains a simplistic program to demonstrate the very basic functionality -> Get images from connected camera, process the image (currently it captures faces) and then send the data to the backend so the web interface can access and display whatever info is there.

Make sure you have the dependencies installed ->
- opencv 4
- Flask
- Flask-socketio

To run, simply run webapp.py and open 127.0.0.1:6969 in your browser