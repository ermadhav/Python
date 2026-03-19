from flask import Flask, render_template, request
import uuid
import os
from werkzeug.utils import secure_filename
from generate_process import generate_reel  # ✅ IMPORTANT

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

UPLOAD_FOLDER = os.path.join(BASE_DIR, 'user_uploads')
OUTPUT_FOLDER = os.path.join(BASE_DIR, 'static', 'output')

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure folders exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/create", methods=['GET', "POST"])
def create():
    video = None

    if request.method == "POST":
        rec_id = request.form.get("uuid")
        desc = request.form.get("text")

        folder_path = os.path.join(app.config['UPLOAD_FOLDER'], rec_id)
        os.makedirs(folder_path, exist_ok=True)

        # Save images
        for file in request.files.values():
            if file and file.filename:
                filename = secure_filename(file.filename)
                file.save(os.path.join(folder_path, filename))

        # Save description
        if desc:
            with open(os.path.join(folder_path, "desc.txt"), "w", encoding="utf-8") as f:
                f.write(desc)

        # ✅ Generate reel
        video = generate_reel(folder_path)

    myid = str(uuid.uuid1())
    return render_template("create.html", myid=myid, video=video)


@app.route("/gallery")
def gallery():
    videos = os.listdir(OUTPUT_FOLDER)
    return render_template("gallery.html", videos=videos)


if __name__ == "__main__":
    app.run(debug=True)