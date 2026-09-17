import cv2
import numpy as np

# Load first image.
image_1 = cv2.imread(
    "Known_Faces/jegathayini.jpg"
)

# Load second image.
image_2 = cv2.imread(
    "Known_Faces/atharsha.jpg"
)

# Check whether images exist.
if image_1 is None or image_2 is None:

    print(
        "Image not found."
    )

    exit()

# Resize images to same dimensions.
image_2 = cv2.resize(
    image_2,
    (
        image_1.shape[1],
        image_1.shape[0]
    )
)

# Calculate difference.
difference = cv2.absdiff(
    image_1,
    image_2
)

# Calculate total difference.
difference_score = np.sum(
    difference
)

# Display result.
print(
    f"Difference Score : {difference_score}"
)