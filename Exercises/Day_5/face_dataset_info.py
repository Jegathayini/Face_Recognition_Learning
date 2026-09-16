import cv2
import os


# Folder containing known face images.
known_faces_folder = "Known_Faces"

# Loop through all files in the folder.
for file_name in os.listdir(
    known_faces_folder
):

    # Create full file path.
    file_path = os.path.join(
        known_faces_folder,
        file_name
    )

    # Load image.
    image = cv2.imread(
        file_path
    )

    # Skip if image cannot be loaded.
    if image is None:

        print(
            f"Could not load: {file_name}"
        )

        continue

    # Extract image dimensions.
    height, width = image.shape[:2]

    # Display information.
    print(
        f"Image Name : {file_name}"
    )

    print(
        f"Width      : {width}"
    )

    print(
        f"Height     : {height}"
    )

    print(
        "-" * 30
    )