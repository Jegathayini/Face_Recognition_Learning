import cv2
import os

# Folder containing employee images.
known_faces_folder = "Known_Faces"

# Create employee database.
employee_database = {}

# Read all employee images.
for file_name in os.listdir(
    known_faces_folder
):

    # Create full image path.
    file_path = os.path.join(
        known_faces_folder,
        file_name
    )

    # Load image.
    image = cv2.imread(
        file_path
    )

    # Skip invalid images.
    if image is None:

        print(
            f"Could not load {file_name}"
        )

        continue

    # Extract employee name.
    employee_name = os.path.splitext(
        file_name
    )[0]

    # Store image in database.
    employee_database[
        employee_name
    ] = image

# Display employee information.
for employee_name in employee_database:

    print(
        f"Employee Loaded : {employee_name}"
    )

print(
    f"\nTotal Employees : {len(employee_database)}"
)