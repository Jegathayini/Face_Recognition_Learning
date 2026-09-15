import cv2
import mediapipe as mp

# Load employee image.
image = cv2.imread(
    "Known_Faces/jegathayini_pic.jpg"
)

# Check whether image exists.
if image is None:

    print(
        "Image not found."
    )

    exit()

# Get original dimensions.
height, width = image.shape[:2]

# Maximum width allowed.
max_width = 800

# Resize only if image is very large.
if width > max_width:

    scale_ratio = max_width / width
    # Calculate scaling factor.

    new_width = int(
        width * scale_ratio
    )

    new_height = int(
        height * scale_ratio
    )

    # Resize while preserving aspect ratio.
    image = cv2.resize(
        image,
        (new_width, new_height)
    )

    print(
        "Image resized successfully."
    )


# Convert BGR to RGB.
rgb_image = cv2.cvtColor(
    image,
    cv2.COLOR_BGR2RGB
)

# Create MediaPipe Face Detector.
FaceDetector = mp.tasks.vision.FaceDetector

print(
    "MediaPipe Face Detector Available ✅"
)

# Display image.
cv2.imshow(
    "Employee Image",
    image
)

cv2.waitKey(0)

cv2.destroyAllWindows()