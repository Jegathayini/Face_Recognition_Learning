import os

# Folder containing registered faces.
known_faces_folder = "Known_Faces"

# Create employee registry.
employee_registry = []

# Read all files from folder.
for file_name in os.listdir(
    known_faces_folder
):

    # Remove file extension.
    employee_name = os.path.splitext(
        file_name
    )[0]

    # Add employee name.
    employee_registry.append(
        employee_name
    )

# Display all employees.
print(
    "Registered Employees"
)

print(
    "-" * 30
)

for employee in employee_registry:

    print(
        employee
    )

print(
    "-" * 30
)

print(
    f"Total Employees : {len(employee_registry)}"
)