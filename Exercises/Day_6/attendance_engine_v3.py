import os
import cv2
import numpy as np

# Directory paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
KNOWN_FACES_DIR = os.path.join(BASE_DIR, "../../Known_faces")

# Built-in OpenCV Face Detector
cascade_path = cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
face_cascade = cv2.CascadeClassifier(cascade_path)

# Initialize OpenCV's built-in LBPH Face Recognizer
recognizer = cv2.face.LBPHFaceRecognizer_create()


def train_recognizer(known_dir):
    """Scans Known_faces, extracts faces, and trains the LBPH model."""
    faces = []
    labels = []
    label_map = {}
    current_label = 0

    if not os.path.exists(known_dir):
        print(f"Error: Directory '{known_dir}' not found.")
        return label_map

    print("Training face recognizer on known database...")

    for filename in os.listdir(known_dir):
        if filename.lower().endswith((".jpg", ".jpeg", ".png")):
            name = os.path.splitext(filename)[0].capitalize()
            img_path = os.path.join(known_dir, filename)
            img = cv2.imread(img_path)

            if img is None:
                continue

            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            detected = face_cascade.detectMultiScale(
                gray, scaleFactor=1.1, minNeighbors=5
            )

            for x, y, w, h in detected:
                face_roi = gray[y : y + h, x : x + w]
                face_roi = cv2.resize(face_roi, (200, 200))

                faces.append(face_roi)
                labels.append(current_label)

            label_map[current_label] = name
            current_label += 1

    if len(faces) > 0:
        recognizer.train(faces, np.array(labels))
        print(
            f"Successfully trained on {len(faces)} profile(s): {list(label_map.values())}"
        )
    else:
        print("Warning: No valid faces found in Known_faces folder.")

    return label_map


# Train on startup
label_map = train_recognizer(KNOWN_FACES_DIR)

# Open Webcam Feed
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not access webcam.")
    exit()

print("Webcam active! Press 'q' to quit.")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    detected_faces = face_cascade.detectMultiScale(
        gray, scaleFactor=1.1, minNeighbors=6, minSize=(60, 60)
    )

    for x, y, w, h in detected_faces:
        face_roi = gray[y : y + h, x : x + w]
        face_roi = cv2.resize(face_roi, (200, 200))

        # LBPH Predict returns: (Label ID, Confidence Distance)
        # Note: Lower confidence score = closer match in LBPH!
        label_id, confidence = recognizer.predict(face_roi)

        # Confidence distance under 75 is considered a reliable match
        if confidence < 75:
            person_name = label_map.get(label_id, "Unknown")
            color = (0, 255, 0)  # Green for recognized
            label_text = f"{person_name} ({int(100 - confidence)}%)"
        else:
            person_name = "Unknown"
            color = (0, 0, 255)  # Red for unknown
            label_text = "Unknown"

        # Draw Bounding Box & Label
        cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
        cv2.rectangle(
            frame, (x, y - 30), (x + len(label_text) * 12, y), color, cv2.FILLED
        )
        cv2.putText(
            frame,
            label_text,
            (x + 5, y - 8),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (255, 255, 255),
            2,
        )

    cv2.imshow("PresenX - Attendance Engine", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()