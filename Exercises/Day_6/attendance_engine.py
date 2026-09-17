import cv2
import csv
from datetime import datetime

# Load face detector.
face_detector = cv2.CascadeClassifier(
    cv2.data.haarcascades +
    "haarcascade_frontalface_default.xml"
)

# Track attendance.
attendance_marked = False

# Open webcam.
camera = cv2.VideoCapture(0)

while True:

    # Capture frame.
    success, frame = camera.read()

    if not success:

        break

    # Convert frame to grayscale.
    gray = cv2.cvtColor(
        frame,
        cv2.COLOR_BGR2GRAY
    )

    # Detect faces.
    faces = face_detector.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5
    )

    # Draw rectangles.
    for (x, y, w, h) in faces:

        cv2.rectangle(
            frame,
            (x, y),
            (x + w, y + h),
            (0, 255, 0),
            2
        )

        # Simulated recognition.
        employee_name = "Jegathayini"

        cv2.putText(
            frame,
            employee_name,
            (x, y - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0, 255, 0),
            2
        )

        # Mark attendance once.
        if not attendance_marked:

            current_time = datetime.now()

            with open(
                "Attendance/attendance.csv",
                "a",
                newline=""
            ) as file:

                writer = csv.writer(
                    file
                )

                writer.writerow(
                    [
                        employee_name,
                        current_time.strftime(
                            "%Y-%m-%d %H:%M:%S"
                        )
                    ]
                )

            print(
                f"{employee_name} marked present ✅"
            )

            attendance_marked = True

    cv2.imshow(
        "PresenX Attendance",
        frame
    )

    if cv2.waitKey(1) == ord("q"):

        break

camera.release()

cv2.destroyAllWindows()