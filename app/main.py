from flask import Flask
app=Flask(__name__)

@app.route("/")
def home_view():
    return"<h1>welcome2233my home<h1>"

