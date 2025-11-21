from flask import Flask, render_template, request, redirect
from video_manager import StreamWatcher
import base64

app = Flask(__name__)
#TODO Change to instead pull from config file.
vid = StreamWatcher("rtsp://localhost:8554/live.sdp", 1)

@app.route("/", methods=["GET", "POST"])
def default():
    if request.method == "POST":
        if request.form.get("reconnect") != None:
            return render_template("index.html", img_url=get_image())
        elif request.form.get("request") != None:
            return  render_template("index.html", img_url=get_image())
        else:
            return "Error - Invalid Request", 400
    return render_template("index.html", img_url="iVBORw0KGgoAAAANSUhEUgAAAAUAAAAFCAYAAACNbyblAAAAHElEQVQI12P4//8/w38GIAXDIBKE0DHxgljNBAAO9TXL0Y4OHwAAAABJRU5ErkJggg==")

def get_image()->str:
    #TODO Broken. No clue how to fix.
    [result, base64image] = vid.capture_frame()
    if result:
        print(base64image)
        return base64image
    else:
        pass