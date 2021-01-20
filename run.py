import os
import json
from datetime import datetime
from flask import Flask, redirect, render_template, request, session, url_for


app = Flask(__name__)
app.secret_key = "randomstring123"
messages = []

def add_message(username, message):
    """Add messages to the messages list"""
    now = datetime.now().strftime("%H:%M:%S")
    # messages_dict = {"timestamp": now, "from": username, "message": message} << instead of this line use the function in the 'append' function below instead
    # messages.append(messages_dict) 
    messages.append({"timestamp": now, "from": username, "message": message}) 
    
# def get_all_messages():
    # """Get all of the messages and seperate them with a 'br'"""
    # return "<br>".join(messages)

@app.route('/', methods = ["GET", "POST"])
def index():
    """Main page with instructions"""

    if request.method == "POST":
        session["username"] = request.form["username"]

    if "username" in session:
        return redirect(url_for("user", username=session["username"]))

    return render_template("index.html")


@app.route('/chat/<username>', methods = ["GET", "POST"])
def user(username):
    """Add and Display chat messages"""

    if request.method == "POST":
        username = session["username"]
        message = request.form["message"]
        add_message(username, message)
        return redirect(url_for("user", username=session["username"]))
    # return "<h1>Welcome, {0}</h1>{1}".format(username, get_all_messages())  
    # return "<h1>Welcome, {0}</h1>{1}".format(username, messages)
    return render_template("chat.html", username = username,
        chat_messages = messages)


app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True
    )