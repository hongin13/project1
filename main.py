from flask import Flask, render_template, request, redirect, url_for, send_from_directory, Response
from werkzeug.utils import secure_filename
import flask
import os
import sys
import matplotlib

import test
import delete

matplotlib.use('TkAgg')

app = Flask(__name__)

@app.route("/")
def show_index():
    return render_template("index.html")

@app.route("/file_upload", methods = ['GET', 'POST'])
def file_upload():
    if request.method == 'POST':
        f = request.files['file']
        f.save('./test/' + secure_filename(f.filename))
        result = test.run()
        delete.run()
        return render_template(result.lower() + '.html')
    else:
        return render_template('file_upload.html')

def main():
    app.run(host="0.0.0.0", debug = True)

if __name__ == "__main__":
    main()