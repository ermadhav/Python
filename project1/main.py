from flask import Flask, render_template, request
import uuid
import os
from werkzeug.utils import secure_filename

# ✅ Base directory (important for correct paths)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# ✅ Upload folder (absolute path)
UPLOAD_FOLDER = os.path.join(BASE_DIR, 'user_uploads')
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# ✅ Ensure base upload folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/create", methods=['GET', "POST"])
def create():
    
    if request.method == "POST":
        rec_id = request.form.get("uuid")
        desc = request.form.get("text")

        # ✅ Create unique folder for this upload
        folder_path = os.path.join(app.config['UPLOAD_FOLDER'], rec_id)
        os.makedirs(folder_path, exist_ok=True)

        # ✅ Save uploaded files
        for file in request.files.values():
            if file and file.filename:
                filename = secure_filename(file.filename)
                file.save(os.path.join(folder_path, filename))

        # ✅ Save description text
        if desc:
            with open(os.path.join(folder_path, "desc.txt"), "w", encoding="utf-8") as f:
                f.write(desc)

    # Generate new UUID for next form
    myid = str(uuid.uuid1())
    return render_template("create.html", myid=myid)


@app.route("/gallery")
def gallery():
    return render_template("gallery.html")


if __name__ == "__main__":
    app.run(debug=True)