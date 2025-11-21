from flask import Flask, render_template, request, redirect
from video_manager import StreamWatcher
import base64

app = Flask(__name__)
vid = StreamWatcher("rtsp://localhost:8554/live.sdp", 1)

@app.route("/", methods=["GET", "POST"])
def default():
    if request.method == "POST":
        if request.form.get("reconnect") != None:
            return render_template("index.html", test="Stream Reconnect Request")
        elif request.form.get("request") != None:
            return  render_template("index.html", test="Frame Request")
        else:
            return "Error - Invalid Request", 400
    return render_template("index.html", test="Normal Request")

def get_image():
    [result, image] = vid.capture_frame()
    if result:
        pass
    else:
        pass