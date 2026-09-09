# Day 1 - Computer Vision Fundamentals

## What is Computer Vision?

Computer Vision is a field of Artificial Intelligence that enables computers to understand and interpret images and videos.

---

## What is an Image?

An image is a collection of pixels arranged in rows and columns.

---

## What is a Pixel?

Pixel stands for **Picture Element**.

A pixel is the smallest unit of a digital image.

---

## What is Resolution?

Resolution represents the width and height of an image.

**Example:**

```text
1920 × 1080
```

This image contains:

```text
1920 × 1080 = 2,073,600 pixels
```

---

## RGB

RGB stands for:

- Red
- Green
- Blue

Colors are represented using intensity values ranging from **0 to 255**.

---

## OpenCV Color Format

Unlike most image applications, OpenCV stores colors in **BGR** format:

- Blue
- Green
- Red

---

## Reading Images

OpenCV reads images using:

```python
img = cv2.imread("image.jpg")
```

This loads the image from storage into memory so it can be processed.

---

## Displaying Images

```python
cv2.imshow("My Image", img)
```

Displays an image in a window.

```python
cv2.waitKey(0)
```

Waits until a key is pressed.

```python
cv2.destroyAllWindows()
```

Closes all OpenCV windows.

---

## Image Shape

```python
print(img.shape)
```

Example Output:

```text
(723, 1000, 3)
```

Meaning:

- Height = 723 pixels
- Width = 1000 pixels
- Channels = 3

---

## Pixels

Images are made up of pixels arranged in rows and columns.

A pixel can be accessed using:

```python
img[row, column]
```

Example:

```python
img[0,0]
```

Output:

```text
[71 68 94]
```

Meaning:

```text
Blue  = 71
Green = 68
Red   = 94
```

---

## Grayscale Images

A grayscale image stores only brightness information instead of color information.

Pixel values range from:

```text
0   = Black
255 = White
```

Grayscale images use a single channel instead of three color channels.

### Converting a Color Image to Grayscale

```python
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
```

### Benefits of Grayscale Images

- Faster image processing
- Less memory usage
- Removes unnecessary color information
- Commonly used in face detection

### Shape Comparison

Color Image:

```python
print(img.shape)
```

Output:

```text
(723, 1000, 3)
```

Grayscale Image:

```python
print(gray.shape)
```

Output:

```text
(723, 1000)
```

---

## Drawing Rectangles

OpenCV can draw rectangles using:

```python
cv2.rectangle()
```

Example:

```python
cv2.rectangle(
    img,
    (100, 100),
    (300, 300),
    (0, 255, 0),
    3
)
```

### Parameters

- Image
- Top-left corner
- Bottom-right corner
- Color (BGR)
- Thickness

Rectangles are commonly used in face detection to highlight detected faces.

---

## Writing Text on Images

OpenCV can write text on images using:

```python
cv2.putText()
```

Example:

```python
cv2.putText(
    img,
    "Hello OpenCV",
    (50, 50),
    cv2.FONT_HERSHEY_SIMPLEX,
    1,
    (0, 255, 0),
    2
)
```

### Parameters

- Image
- Text
- Position
- Font Style
- Font Size
- Color (BGR)
- Thickness

This is commonly used to display:

- Names
- Labels
- Confidence Scores
- Recognition Results

---

## Key Takeaways

- Images are collections of pixels.
- Pixels contain numerical color information.
- OpenCV stores color images in BGR format.
- Images are loaded into memory using `cv2.imread()`.
- Grayscale images contain a single brightness channel.
- Rectangles and text can be drawn on images for visualization.
- These concepts form the foundation for Face Detection and Face Recognition.

## Webcam and Frames

OpenCV accesses webcams using:

```python
cv2.VideoCapture(0)
```

A video is a collection of frames displayed rapidly.

Frame:

- A single image captured from the webcam.

Example:

```python
success, frame = camera.read()
```

Returns:

- success -> indicates if frame capture succeeded
- frame -> captured image

A webcam stream is created by continuously reading and displaying frames.

Workflow:

```text
Webcam
↓
Capture Frame
↓
Display Frame
↓
Repeat
```