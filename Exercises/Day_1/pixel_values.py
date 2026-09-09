import cv2
# Bring OpenCV library into this program.

img = cv2.imread("Exercises/Day_1/pragg_03.jpg")
# Read the image and load it into memory.

print("Top Left Pixel:", img[0, 0])
# First pixel of the image.

print("Second Pixel:", img[0, 1])
# Pixel next to the first one.

print("Pixel at Row 100 Column 100:", img[100, 100])
# A pixel somewhere inside the image.