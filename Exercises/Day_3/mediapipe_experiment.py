import mediapipe as mp
# Bring MediaPipe library into this program.


print("Version:", mp.__version__)
# Display installed MediaPipe version.


print("\nTasks:")
print(dir(mp.tasks))
# Display available task categories.


print("\nVision:")
print(dir(mp.tasks.vision))
# Display available computer vision tasks.