import cv2
import numpy as np

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

# Calculate average pixel value.
average_pixel = np.mean(
    image
)

# Calculate brightest pixel.
max_pixel = np.max(
    image
)

# Calculate darkest pixel.
min_pixel = np.min(
    image
)

# Display statistics.
print(
    f"Average Pixel : {average_pixel}"
)

print(
    f"Brightest Pixel : {max_pixel}"
)

print(
    f"Darkest Pixel : {min_pixel}"
)