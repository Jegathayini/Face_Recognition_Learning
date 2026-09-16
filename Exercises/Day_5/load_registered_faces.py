import cv2
import os

# Folder containing registered faces.
known_faces_folder = "Known_Faces"

# Loop through all registered faces.
for file_name in os.listdir(
    known_faces_folder
):

    # Create full path.
    file_path = os.path.join(
        known_faces_folder,
        file_name
    )

    # Load image.
    image = cv2.imread(
        file_path
    )

    # Check whether image was loaded.
    if image is None:

        print(
            f"Could not load: {file_name}"
        )

        continue

    # Get image dimensions.
    height, width = image.shape[:2]

    print(
        f"Face Loaded: {file_name}"
    )

    print(
        f"Width : {width}"
    )

    print(
        f"Height : {height}"
    )

    print(
        "-" * 30
    )