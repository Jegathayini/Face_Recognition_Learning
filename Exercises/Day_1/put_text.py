import cv2
# Bring OpenCV library into this program.

img = cv2.imread("Exercises/Day_1/pragg_03.jpg")
# Read the image and load it into memory.

cv2.putText(
    img,
    "Hello OpenCV",
    (300, 300),
    cv2.FONT_HERSHEY_SIMPLEX,
    1,
    (0, 255, 0),
    2
)
# Draw text on the image.
#
# img                         -> image to draw on
# "Hello OpenCV"              -> text to display
# (50,50)                     -> starting position of text
# cv2.FONT_HERSHEY_SIMPLEX    -> font style
# 1                           -> font scale (size)
# (0,255,0)                   -> text color (Green in BGR)
# 2                           -> thickness

cv2.imshow("Text Example", img)
# Display image with text.

cv2.waitKey(0)
# Wait until a key is pressed.

cv2.destroyAllWindows()
# Close all windows.