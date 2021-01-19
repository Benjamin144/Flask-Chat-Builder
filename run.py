import os
import json
from flask import Flask


app = Flask(__name__)

@app.route('/')
def index():
    """Main page with instructions"""
    return "<h1>To send a message use /USERNAME/MESSAGE"


@app.route('/<username>')
def user(username):
      return "Hi " + username


@app.route('/<username>/<message>')
def send_message(username, message):
    return "{0}: {1}".format(username, message)


app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True
    )