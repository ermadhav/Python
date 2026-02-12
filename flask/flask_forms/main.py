from flask import Flask,request, render_template

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def hello_world():
    print(request.method)
    print(request.form)
    return render_template("contact.html")

app.run(debug=True)