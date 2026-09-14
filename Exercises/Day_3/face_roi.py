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
# Read image from storage.


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
# Display number of detected faces.


for (x, y, w, h) in faces:
    # Loop through all detected faces.

    print(
        f"x={x}, y={y}, w={w}, h={h}"
    )
    # Display face coordinates.

    cv2.rectangle(
        img,
        (x, y),
        (x + w, y + h),
        (0, 255, 0),
        3
    )
    # Draw green rectangle around face.

    face_roi = img[
        y:y+h,
        x:x+w
    ]
    # Extract only the face region.

    cv2.imshow(
        "Cropped Face",
        face_roi
    )
    # Display cropped face.

    cv2.imwrite(
    "Known_Faces/cropped_face.jpg",
    face_roi
    )
    # Save cropped face.


height, width, _ = img.shape
# Get original image dimensions.


new_width = 800
# Desired display width.


new_height = int(
    height * (new_width / width)
)
# Calculate height while preserving aspect ratio.


img = cv2.resize(
    img,
    (new_width, new_height)
)
# Resize image without distortion.


cv2.imshow(
    "Original Image",
    img
)
# Display original image with rectangle.


cv2.waitKey(0)
# Wait until a key is pressed.


cv2.destroyAllWindows()
# Close all OpenCV windows.