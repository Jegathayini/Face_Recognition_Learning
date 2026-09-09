import cv2
# Bring OpenCV library into this program.

img = cv2.imread("Exercises/Day_1/pragg_03.jpg")
# Read the image and load it into memory.

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Convert the color image into a grayscale image.

cv2.imshow("Original Image", img)
# Display the original color image.

cv2.imshow("Grayscale Image", gray)
# Display the grayscale version.

cv2.waitKey(0)
# Wait until a key is pressed.

cv2.destroyAllWindows()
# Close all OpenCV windows.