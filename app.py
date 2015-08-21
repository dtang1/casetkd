from flask import Flask
from flask import render_template, redirect, url_for
from flask import session, request
from flask import url_for, request, session, redirect


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("home.html")

@app.route("/about/")
def about():
	return render_template("about.html")

@app.route("/information/")
def info():
    return render_template("info.html")

@app.route("/members/")
def members():
	return render_template("members.html")

@app.route("/contact/")
def contact():
    return render_template("contact.html")

@app.route("/history/")
def hisotry():
	return render_template("history.html")

@app.route("/requirements/")
def requirements():
    return render_template("requirements.html")

@app.route("/events/")
def events():
	return render_template("events.html")





if __name__ == "__main__":
        app.run(debug = True)