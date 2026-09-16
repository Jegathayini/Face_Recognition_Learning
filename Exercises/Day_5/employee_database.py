import os

# Folder containing registered faces.
known_faces_folder = "Known_Faces"

# Create employee database.
employee_database = {}

# Read all files from folder.
for file_name in os.listdir(
    known_faces_folder
):

    # Extract employee name.
    employee_name = os.path.splitext(
        file_name
    )[0]

    # Create image path.
    image_path = os.path.join(
        known_faces_folder,
        file_name
    )

    # Store employee information.
    employee_database[
        employee_name
    ] = image_path

# Display database.
print(
    "\nEmployee Database"
)

print(
    "-" * 40
)

for employee_name, image_path in employee_database.items():

    print(
        f"Employee : {employee_name}"
    )

    print(
        f"Image    : {image_path}"
    )

    print(
        "-" * 40
    )