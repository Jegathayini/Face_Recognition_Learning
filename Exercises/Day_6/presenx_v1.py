import cv2
import os

# Folder containing registered employees.
known_faces_folder = "Known_Faces"

# Create employee database.
employee_database = {}

# Read all registered employees.
for file_name in os.listdir(
    known_faces_folder
):

    # Remove extension.
    employee_name = os.path.splitext(
        file_name
    )[0]

    # Store employee.
    employee_database[
        employee_name
    ] = file_name

# Display registry.
print(
    "Registered Employees"
)

print(
    "-" * 30
)

for employee in employee_database:

    print(
        employee
    )

print(
    "-" * 30
)

# Open webcam.
camera = cv2.VideoCapture(0)

while True:

    success, frame = camera.read()

    if not success:

        break

    cv2.putText(
        frame,
        "PRESENX V1",
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        2
    )

    cv2.imshow(
        "PresenX",
        frame
    )

    # Press q to quit.
    if cv2.waitKey(1) == ord("q"):

        break

camera.release()

cv2.destroyAllWindows()