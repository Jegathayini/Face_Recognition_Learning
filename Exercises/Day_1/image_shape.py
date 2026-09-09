import cv2

img = cv2.imread("Exercises/Day_1/pragg_03.jpg")

if img is None:
    print("Image not found!")
else:
    print("Image loaded successfully!")
    print(img.shape)