from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    marks={
        "Madhav": 45,
        "Mahi":40,
        "Anisha": 35,
        "Tanishq": 20,
        "Arpita": 35
    }
    return render_template("index.html", marks = marks)
app.run(debug = True)
