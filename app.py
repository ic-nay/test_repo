from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def default():
    if request.method == 'GET':
        return render_template("index.html")
    elif request.method  == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            return redirect(request.url)
        if file:
            return process_image()
    return "Error", 400

def process_image():
    return "TEST", 200