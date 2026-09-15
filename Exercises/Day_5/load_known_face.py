import cv2

# Load image.
image = cv2.imread(
    "Known_Faces/jegathayini_pic.jpg"
)

# Check whether image exists.
if image is None:

    print(
        "Image not found."
    )

else:

    # Get original dimensions.
    height, width = image.shape[:2]

    # Define new width.
    new_width = 300

    # Calculate proportional height.
    new_height = int(
        height * (new_width / width)
    )

    # Resize without distortion.
    image = cv2.resize(
        image,
        (new_width, new_height)
    )

    print(
        "Image loaded successfully."
    )

    print(
        image.shape
    )

    # Display image.
    cv2.imshow(
        "Known Face",
        image
    )

    cv2.waitKey(0)

    cv2.destroyAllWindows()