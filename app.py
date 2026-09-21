import os
import cv2
import pickle
import numpy as np

from flask import Flask, render_template, request
from insightface.app import FaceAnalysis

app = Flask(__name__)

KNOWN_FACES_DIR = "Known_faces"
EMBEDDINGS_FILE = "Embeddings/embeddings.pkl"

# -----------------------------
# InsightFace
# -----------------------------
face_app = FaceAnalysis(
    name="buffalo_l",
    providers=["CPUExecutionProvider"]
)

face_app.prepare(ctx_id=-1, det_size=(320, 320))

# -----------------------------
# Helpers
# -----------------------------
def normalize_embedding(embedding):
    embedding = np.asarray(embedding, dtype=np.float32)
    norm = np.linalg.norm(embedding)

    if norm == 0:
        return embedding

    return embedding / norm


def generate_embedding(image_path):
    image = cv2.imread(image_path)

    if image is None:
        return None

    faces = face_app.get(image)

    if not faces:
        return None

    face = max(
        faces,
        key=lambda f:
        (f.bbox[2] - f.bbox[0]) *
        (f.bbox[3] - f.bbox[1])
    )

    return normalize_embedding(face.embedding)


def load_database():
    if os.path.exists(EMBEDDINGS_FILE):
        with open(EMBEDDINGS_FILE, "rb") as f:
            return pickle.load(f)

    return {}


def save_database(database):
    with open(EMBEDDINGS_FILE, "wb") as f:
        pickle.dump(database, f)


# -----------------------------
# Routes
# -----------------------------
@app.route("/")
def home():
    return render_template("add_employee.html")


@app.route("/add_employee", methods=["POST"])
def add_employee():

    print("HEY BROOO FORM RECEIVED")

    print("FORM:", request.form)
    print("FILES:", request.files)

    return "Debug Done"

    filename = f"{employee_name}.jpg"
    image_path = os.path.join(
        KNOWN_FACES_DIR,
        filename
    )

    image.save(image_path)

    embedding = generate_embedding(image_path)

    if embedding is None:
        return "No face detected!"

    database = load_database()

    database[employee_name] = [embedding]

    save_database(database)

    return f"{employee_name} added successfully!"


if __name__ == "__main__":
    app.run(debug=True)