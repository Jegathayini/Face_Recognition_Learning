import cv2
# Bring the OpenCV library into this program.
img = cv2.imread("Exercises/Day_1/pragg_03.jpg")
# Reads the image and load it into the memory
cv2.imshow("My Image", img)
# Create a window named "My Image" and display the image stored in img.
cv2.waitKey(0)
# The program pauses until I press a key
# Why 0?
# Wait forever until a key is pressed
cv2.destroyAllWindows()
# Closes all windows
