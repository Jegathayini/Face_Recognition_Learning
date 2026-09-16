import cv2

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

# Display first pixel value.
print(
    image[0][0]
)

# Display center pixel value.
height, width = image.shape[:2]

print(
    image[
        height // 2
    ][
        width // 2
    ]
)
