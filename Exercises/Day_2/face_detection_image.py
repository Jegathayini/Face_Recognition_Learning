import cv2
# Bring OpenCV library into this program.

face_detector = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)
# Load OpenCV's built-in face detector.

img = cv2.imread("Exercises/Day_1/pragg_03.jpg")
# Read the image and load it into memory.

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Convert image to grayscale.

faces = face_detector.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=10
)
# Detect faces.

for (x, y, w, h) in faces:

    cv2.rectangle(
        img,
        (x, y),
        (x + w, y + h),
        (0, 255, 0),
        3
    )
    # Draw rectangle around detected face.

cv2.imshow("Detected Faces", img)
# Display image.

cv2.waitKey(0)
# Wait until user presses a key.

cv2.destroyAllWindows()
# Close windows.