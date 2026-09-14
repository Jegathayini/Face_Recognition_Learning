import cv2
# Bring OpenCV library into this program.


face_detector = cv2.CascadeClassifier(
    cv2.data.haarcascades +
    "haarcascade_frontalface_default.xml"
)
# Load Haar Cascade face detector.


img = cv2.imread(
    "Known_Faces/group_photo.jpg"
)
# Read image.


gray = cv2.cvtColor(
    img,
    cv2.COLOR_BGR2GRAY
)
# Convert image to grayscale.


faces = face_detector.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=7
)
# Detect faces.


print("Faces detected:", len(faces))


face_count = 1
# Counter for naming face images.


for (x, y, w, h) in faces:

    cv2.rectangle(
        img,
        (x, y),
        (x + w, y + h),
        (0, 255, 0),
        3
    )
    # Draw rectangle around face.

    face_roi = img[
        y:y+h,
        x:x+w
    ]
    # Crop face.

    cv2.imwrite(
        f"Known_Faces/face_{face_count}.jpg",
        face_roi
    )
    # Save cropped face.

    face_count += 1


cv2.imshow(
    "Detected Faces",
    img
)

cv2.waitKey(0)

cv2.destroyAllWindows()