#/usr/bin/env python3

from flask import Flask, request, render_template, send_file, url_for
from services.encrypter import passProtect
import os
import subprocess
import json

app = Flask(__name__)

@app.route('/')
def home():

    return render_template("index.html")

@app.route('/download/<path:filename>')
def download(filename):
    return send_file('encrypted/'+filename, as_attachment=True)


@app.route('/upload', methods = ['POST'])
def upload_file():
    try:
        auto_clean()
    except:
        print("Could not clean directories.")
    password = request.form.get('text')
    uploaded_file = request.files.get('file')

    uploaded_file.save('uploads/'+uploaded_file.filename)
    passProtect(uploaded_file.filename, password)

    return json.dumps({"downloadUrl":f"{request.host_url}download/encrypted_{uploaded_file.filename}"})

def auto_clean():
    for file in os.listdir('encrypted/'):
        subprocess.run(["rm",f"encrypted/{file}"])
    for file in os.listdir('uploads/'):
        subprocess.run(["rm",f"uploads/{file}"])
    # shutil.rmtree(os.getcwd()+'/uploads/')

if __name__ == '__main__':
    app.run(debug=True, host = 'localhost', port=int(os.environ.get('PORT', 8080)))