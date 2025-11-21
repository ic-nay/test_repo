from flask import Flask, render_template, request, redirect
from video_manager import StreamWatcher

app = Flask(__name__)
vid = StreamWatcher("rtsp://localhost:8554/live.sdp", 1)

@app.route("/")
def default():
    return render_template("index.html")