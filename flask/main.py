from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/services")
def home():
    return render_template("home.html")

@app.route("/contact")
def home():
    return render_template("home.html")

@app.route("/about")
def home():
    return render_template("home.html")

app.run