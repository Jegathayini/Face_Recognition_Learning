import cv2
# Bring OpenCV library into this program.

face_detector = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)
# Load the Haar Cascade face detector.

camera = cv2.VideoCapture(0)
# Open the default webcam.

while True:
    # Keep capturing frames continuously.

    success, frame = camera.read()
    # Capture a frame from the webcam.

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Convert frame to grayscale.

    faces = face_detector.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=8
    )
    # Detect faces in the frame.

    for (x, y, w, h) in faces:
        # Loop through detected faces.

        cv2.rectangle(
            frame,
            (x, y),
            (x + w, y + h),
            (0, 255, 0),
            3
        )
        # Draw rectangle around face.

    cv2.imshow("Real Time Face Detection", frame)
    # Display the frame.

    if cv2.waitKey(1) == 27:
        # ESC key
        break

camera.release()
# Release webcam.

cv2.destroyAllWindows()
# Close all windows.