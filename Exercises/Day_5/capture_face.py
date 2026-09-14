import cv2
# Bring OpenCV library into this program.


face_detector = cv2.CascadeClassifier(
    cv2.data.haarcascades +
    "haarcascade_frontalface_default.xml"
)
# Load face detector.


camera = cv2.VideoCapture(0)
# Open webcam.


while True:

    success, frame = camera.read()
    # Capture frame.

    gray = cv2.cvtColor(
        frame,
        cv2.COLOR_BGR2GRAY
    )
    # Convert frame to grayscale.

    faces = face_detector.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=7
    )
    # Detect faces.

    for (x, y, w, h) in faces:

        cv2.rectangle(
            frame,
            (x, y),
            (x + w, y + h),
            (0, 255, 0),
            3
        )

        face_roi = frame[
            y:y+h,
            x:x+w
        ]
        # Extract face.

        cv2.putText(
            frame,
            "Press S To Save",
            (x, y - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (0, 255, 0),
            2
        )

    cv2.imshow(
        "Capture Face",
        frame
    )

    key = cv2.waitKey(1)

    if key == ord("s"):
        cv2.imwrite(
            "Known_Faces/webcam_face.jpg",
            face_roi
        )
        print("Face saved successfully.")
        break

    if key == ord("q"):
        break


camera.release()

cv2.destroyAllWindows()
