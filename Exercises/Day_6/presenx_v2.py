import cv2
import os

# Load face detector.
face_detector = cv2.CascadeClassifier(
    cv2.data.haarcascades +
    "haarcascade_frontalface_default.xml"
)

# Folder containing employee images.
known_faces_folder = "Known_Faces"

# Create employee database.
employee_database = {}

# Read all registered employees.
for file_name in os.listdir(
    known_faces_folder
):

    # Remove file extension.
    employee_name = os.path.splitext(
        file_name
    )[0]

    # Store employee.
    employee_database[
        employee_name
    ] = file_name

# Display registered employees.
print(
    "Registered Employees"
)

print(
    "-" * 30
)

for employee in employee_database:

    print(
        employee
    )

print(
    "-" * 30
)

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

    # Draw rectangle around faces.
    for (x, y, w, h) in faces:

        cv2.rectangle(
            frame,
            (x, y),
            (x + w, y + h),
            (0, 255, 0),
            2
        )

        cv2.putText(
            frame,
            "Face Found",
            (x, y - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0, 255, 0),
            2
        )

    cv2.imshow(
        "PresenX V2",
        frame
    )

    # Press q to quit.
    if cv2.waitKey(1) == ord("q"):

        break

camera.release()

cv2.destroyAllWindows()