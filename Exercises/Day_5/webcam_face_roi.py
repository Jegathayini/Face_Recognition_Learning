import cv2
import mediapipe as mp

# Create MediaPipe Face Detector
FaceDetector = mp.tasks.vision.FaceDetector

print("MediaPipe is working ✅")

# Open webcam
camera = cv2.VideoCapture(0)

while True:

    success, frame = camera.read()

    if not success:
        break

    cv2.imshow(
        "MediaPipe Webcam",
        frame
    )

    if cv2.waitKey(1) == ord("q"):
        break

camera.release()
cv2.destroyAllWindows()