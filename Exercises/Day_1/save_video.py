import cv2
# Bring OpenCV library into this program.

camera = cv2.VideoCapture(0)
# Open the default webcam.

fourcc = cv2.VideoWriter_fourcc(*'XVID')
# Define the video codec.

video = cv2.VideoWriter(
    "recorded_video.avi",
    fourcc,
    20.0,
    (640, 480)
)
# Create a video file.
#
# Name      -> recorded_video.avi
# FPS       -> 20
# Resolution-> 640x480

while True:

    success, frame = camera.read()
    # Capture a frame from the webcam.

    video.write(frame)
    # Save the frame into the video file.

    cv2.imshow("Webcam", frame)
    # Display the frame.

    if cv2.waitKey(1) == 27:
        break

camera.release()
# Release webcam.

video.release()
# Save and close video file.

cv2.destroyAllWindows()
# Close all windows.
