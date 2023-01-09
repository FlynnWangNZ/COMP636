import re
from flask import Flask
from datetime import datetime
from flask import render_template
from flask import request

app = Flask(__name__)


@app.route("/")
def root():
    return "Hello, Flask!"


@app.route("/hello/<name>")
def hello_there(name):
    now = datetime.now()
    formatted_now = now.strftime("%A, %d %B, %Y at %X")

    match_object = re.match("[a-zA-Z]+", name)

    if match_object:
        clear_name = name
    else:
        clear_name = 'Friend'
    
    content = "hello there, " + clear_name + '! It is ' + formatted_now
    return content

@app.route("/temp/hello/<name>", methods=["GET", "POST"])
def template(name):
    if request.method == 'GET':
        print(request.args)
    else:
        print(request.form)

    return render_template(
        'index.html', 
        name=name,
        date=datetime.now(),
        request_method=request.method
    )
