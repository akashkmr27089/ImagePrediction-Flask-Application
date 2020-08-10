#!/usr/bin/env python
# coding: utf-8

from datetime import datetime
from flask import Flask, render_template, request 

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/time", methods=['POST'])
def timing():
    return render_template('index.html', current_timmings = str(datetime.now()))

@app.route("/doc_upload",methods=["POST"])
def upload_file():
    print(request.form)
    data = [int(x) for x in request.form.values()]
    return render_template('fileupload.html', first_arg = str(data[1]), second_arg = str(data[0]))

@app.route('/test3', methods=["POST"])
def upload_images():
    print(dir(request))
    data = request.files['fileToUpload']
    print(data)
    return 'done'
    

@app.route("/upload")
def uploading():
    return render_template('upload_files.html')

@app.route('/test')
def test():
    return render_template('fileupload.html')


if __name__ == "__main__":
    app.run(debug=True)