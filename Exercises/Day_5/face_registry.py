import os

# Folder containing registered faces.
known_faces_folder = "Known_Faces"

# Create empty registry.
face_registry = []

# Read all files from the folder.
for file_name in os.listdir(
    known_faces_folder
):

    # Add file name to registry.
    face_registry.append(
        file_name
    )

# Display registered faces.
print(
    "Registered Faces"
)

print(
    "-" * 30
)

for face_name in face_registry:

    print(
        face_name
    )

# Display total count.
print(
    "-" * 30
)

print(
    f"Total Registered Faces : {len(face_registry)}"
)