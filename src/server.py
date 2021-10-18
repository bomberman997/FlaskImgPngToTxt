from flask import Flask, render_template, request, redirect, url_for,send_file
from werkzeug.utils import secure_filename
from tessUtils import imageToCsv
from tessUtils import imageToTxt
import os


UPLOAD_FOLDER = '/output/'
app = Flask(__name__)

@app.route('/')
def index():
    return "Hello"

@app.route("/addfile", methods=['POST','PUT'])
def receive_file():
    file = request.files['file']
    filename=secure_filename(file.filename)
    filename = '/output/'+filename
    file.save(filename)
    imageToTxt(filename)
    return filename

@app.route('/return-files/<filename>')
def return_files_tut(filename):
    file_path = UPLOAD_FOLDER + filename
    return send_file(file_path, as_attachment=True, attachment_filename='')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port = 8080, threaded = True, debug = True)
