from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, Cosmo Coder!</p>"

app.run(debug = True)