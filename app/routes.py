from app import app
from flask import render_template, request
from app.models import model

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/results', methods = ["POST", "GET"])
def results():
    #stores data as dictionary
    userdata = dict(request.form)
    print(userdata)
    output = model.password(userdata)
    print(output)
    return render_template("results.html", output = output)
