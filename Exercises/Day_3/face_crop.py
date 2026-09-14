import cv2

face_detector = cv2.CascadeClassifier(
    cv2.data.haarcascades +
    "haarcascade_frontalface_default.xml"
)

img = cv2.imread(
    "Known_Faces/jegathayini_pic.jpg"
)

print("Image Shape:", img.shape)

gray = cv2.cvtColor(
    img,
    cv2.COLOR_BGR2GRAY
)

faces = face_detector.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=10
)

print("Faces detected:", len(faces))

for (x, y, w, h) in faces:

    print(
        f"x={x}, y={y}, w={w}, h={h}"
    )

    cv2.rectangle(
        img,
        (x, y),
        (x + w, y + h),
        (0, 255, 0),
        5
    )
height, width, _ = img.shape

new_width = 800

new_height = int(
    height * (new_width / width)
)

img = cv2.resize(
    img,
    (new_width, new_height)
)
# Resize image for better viewing.
cv2.imshow(
    "Original Image",
    img
)

cv2.waitKey(0)

cv2.destroyAllWindows()