import cv2
# Bring OpenCV library into this program.

img = cv2.imread("Exercises/Day_1/pragg_03.jpg")
# Read the image and load it into memory.

cv2.rectangle(img, (100, 100), (300, 300), (0, 255, 0), 3)
# Draw a green rectangle on the image.
#
# img             -> image to draw on
# (100,100)       -> top-left corner
# (300,300)       -> bottom-right corner
# (0,255,0)       -> green color in BGR
# 3               -> line thickness

cv2.imshow("Rectangle", img)
# Display image with rectangle.

cv2.waitKey(0)
# Wait until a key is pressed.

cv2.destroyAllWindows()
# Close all windows.