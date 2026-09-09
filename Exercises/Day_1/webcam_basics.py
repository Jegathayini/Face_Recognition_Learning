import cv2
# Bring OpenCV library into this program.

camera = cv2.VideoCapture(0)
# Open the default webcam.

while True:
    # Run continuously.

    success, frame = camera.read()
    # Capture a frame from the webcam.
    #
    # success -> True if frame captured successfully
    # frame   -> image captured from camera

    cv2.imshow("Webcam", frame)
    # Display the current frame.

    if cv2.waitKey(1) == 27:
        # 27 represents the ESC key.
        break

camera.release()
# Release the webcam.

cv2.destroyAllWindows()
# Close all OpenCV windows.
