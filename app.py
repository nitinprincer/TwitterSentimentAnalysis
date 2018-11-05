import os, zipfile
from flask import Flask, render_template, flash, request, url_for, redirect, Response, send_file
from functions import credentials, model_run
from os import remove,path
from werkzeug.utils import secure_filename
import json
import pandas as pd
import sys

app = Flask(__name__)
# set as part of the config
SECRET_KEY = 'many random bytes'
# or set directly on the app
app.secret_key = 'many random bytes'

@app.route('/')
def homepage():
    print("main hiiiii")
    return render_template("main.html")

@app.route('/dashboard/', methods=["GET","POST"])
def dashboard():
    print("dashboard hiiiiiiiiiii")
    error = ''
    try:
        if request.method == "POST":
            attempted_username = request.form['username']
            attempted_password = request.form['password']
            credt=credentials()
            lst=credt[attempted_username]
            if attempted_username in credt and lst[0]==attempted_password:
                print("sucess!!!!")
                return render_template("dashboard.html")
            else:
                error = "Invalid credentials. Try Again."
                print(error)
                flash(error)
        return render_template("main.html", error = error)
    except Exception as e:
        flash(e)
        print(e)
        return render_template("main.html", error = error)

@app.route('/upload/', methods=['GET','POST'])
def upload_file(): 
    print("upload hiiiiiiiiiii")
    error = ''
    try:
        if request.method == 'POST':
           txt=request.form['txt']
           df=model_run(txt,app.root_path)
           return render_template("view.html",table=df.to_html(), titles = 'tweets O/P')
        error = "error getting request"
        return render_template("dashboard.html", error = error)
    except Exception as e:
        flash(e)
        print(e)
        return render_template("dashboard.html", error = error)

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

@app.route('/getCSV/')
def getCSV():
    try:
        file_path=os.path.join(app.root_path,'final.csv')
        return send_file(file_path, attachment_filename='twitter.csv',as_attachment=True)
    except Exception as e:
        return str(e)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
