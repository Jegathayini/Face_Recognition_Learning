import cv2

# Load employee image.
image = cv2.imread(
    "Known_Faces/jegathayini.jpg"
)

# Check whether image exists.
if image is None:

    print(
        "Image not found."
    )

    exit()

# Display total pixel count.
height, width = image.shape[:2]

total_pixels = (
    height *
    width
)

print(
    f"Height : {height}"
)

print(
    f"Width : {width}"
)

print(
    f"Total Pixels : {total_pixels}"
)