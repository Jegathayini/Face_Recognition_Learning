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

# Display image information.
print(
    f"Shape : {image.shape}"
)

print(
    f"Height : {image.shape[0]}"
)

print(
    f"Width : {image.shape[1]}"
)

print(
    f"Channels : {image.shape[2]}"
)