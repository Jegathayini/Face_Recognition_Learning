import cv2
# Bring OpenCV library into this program.


face_detector = cv2.CascadeClassifier(
    cv2.data.haarcascades +
    "haarcascade_frontalface_default.xml"
)
# Load Haar Cascade face detector.


img = cv2.imread(
    "Known_Faces/jegathayini_pic.jpg"
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


for (x, y, w, h) in faces:

    cv2.rectangle(
        img,
        (x, y),
        (x + w, y + h),
        (0, 255, 0),
        3
    )
    # Draw rectangle.


    cv2.putText(
        img,
        "Face Found",
        (x, y - 10),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (0, 255, 0),
        2
    )
    # Display text above face.


height, width, _ = img.shape

new_width = 800

new_height = int(
    height * (new_width / width)
)

img = cv2.resize(
    img,
    (new_width, new_height)
)

cv2.imshow(
    "Face Labeling",
    img
)

cv2.waitKey(0)

cv2.destroyAllWindows()