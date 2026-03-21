from flask import Flask, render_template, request, redirect, url_for
import uuid
from werkzeug.utils import secure_filename
import os
from generate_process import text_to_audio, create_reel

UPLOAD_FOLDER = 'user_uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


# ✅ Helper function for file validation
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/create", methods=["GET", "POST"])
def create():
    myid = str(uuid.uuid1())

    if request.method == "POST":
        rec_id = request.form.get("uuid")
        desc = request.form.get("text")

        # ✅ Get multiple files correctly
        files = request.files.getlist("images")

        input_files = []

        # ✅ Create folder safely
        upload_path = os.path.join(app.config['UPLOAD_FOLDER'], rec_id)
        os.makedirs(upload_path, exist_ok=True)

        # ✅ Save uploaded files
        for file in files:
            if file and file.filename != '':
                if allowed_file(file.filename):
                    # Optional: unique filename to avoid conflicts
                    filename = str(uuid.uuid4()) + "_" + secure_filename(file.filename)

                    file.save(os.path.join(upload_path, filename))
                    input_files.append(filename)
                    print("Saved:", filename)

        # ✅ Save description
        with open(os.path.join(upload_path, "desc.txt"), "w") as f:
            f.write(desc if desc else "")

        # ✅ Create input.txt
        input_txt_path = os.path.join(upload_path, "input.txt")
        with open(input_txt_path, "w") as f:
            for fl in input_files:
                f.write(f"file '{fl}'\n")
                f.write("duration 1\n")

        # ✅ Generate audio & reel
        text_to_audio(rec_id)
        create_reel(rec_id)

        return redirect(url_for('gallery'))

    return render_template("create.html", myid=myid)


@app.route("/gallery")
def gallery():
    reels_path = "static/reels"

    # Ensure folder exists
    os.makedirs(reels_path, exist_ok=True)

    reels = os.listdir(reels_path)
    print(reels)

    return render_template("gallery.html", reels=reels)


if __name__ == "__main__":
    app.run(debug=True)