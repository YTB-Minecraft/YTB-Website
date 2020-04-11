import flask
from flask import Flask
from flask import request
app = Flask(__name__)

@app.route("/")
def index():
    return "Hello World"
app.run(port=80, debug=True)