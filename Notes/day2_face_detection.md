# Day 2 - Face Detection

## What is Face Detection?

Face Detection is the process of locating faces within an image or video.

Face Detection answers:

> "Is there a face present?"

It does not identify who the person is.

---

## Face Detection vs Face Recognition

### Face Detection

Answers:

```text
Is there a face?
```

Output:

```text
Face Found
```

### Face Recognition

Answers:

```text
Whose face is this?
```

Output:

```text
Officer Identified
```

---

## Haar Cascade Classifier

Haar Cascade is a machine learning based object detection technique used for face detection.

It detects faces by scanning different regions of an image and comparing them against learned facial patterns.

A Haar Cascade model is loaded using:

```python
face_detector = cv2.CascadeClassifier(...)
```

The facial knowledge is stored in a pre-trained model file called:

```text
haarcascade_frontalface_default.xml
```

This file contains learned facial patterns obtained from training on thousands of face and non-face images.

---

## Why Grayscale is Used

Face detection focuses on:

- Patterns
- Edges
- Contrast

rather than color information.

Benefits:

- Faster processing
- Less memory usage
- Improved Haar Cascade performance
- Removes unnecessary color information

Example:

```python
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
```

---

## Face Detection Workflow

```text
Image
↓
Convert to Grayscale
↓
Load Haar Cascade Model
↓
Detect Face
↓
Get Face Coordinates
↓
Draw Rectangle
↓
Display Result
```

---

## detectMultiScale()

Face detection is performed using:

```python
detectMultiScale()
```

Example:

```python
faces = face_detector.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=8
)
```

The function scans the image at multiple scales and returns the coordinates of detected faces.

---

## Face Coordinates

The detector returns:

```text
x, y, w, h
```

Where:

- x = Horizontal position
- y = Vertical position
- w = Width of the face
- h = Height of the face

These coordinates are used to draw rectangles around detected faces.

---

## Drawing Face Boundaries

Example:

```python
cv2.rectangle(
    img,
    (x, y),
    (x + w, y + h),
    (0, 255, 0),
    3
)
```

This draws a green rectangle around each detected face.

---

## False Positives

A false positive occurs when the detector incorrectly identifies a non-face object as a face.

Example:

- Actual face detected ✅
- Background object detected as a face ❌

Haar Cascades can sometimes confuse objects and patterns with facial structures because they rely on visual patterns rather than true image understanding.

---

## minNeighbors

The `minNeighbors` parameter controls how strict the detector is.

Lower values:

- More detections
- More false positives

Higher values:

- Fewer detections
- More reliable detections

Typical values:

```python
5 - 10
```

Example:

```python
minNeighbors = 8
```

Increasing this value can reduce false positives but may also miss some real faces.

---

## Key Takeaways

- Face Detection locates faces but does not identify people.
- Haar Cascade is a pre-trained face detection model.
- Grayscale images improve detection efficiency.
- detectMultiScale() scans images at multiple sizes.
- Face detection returns face coordinates.
- False positives can occur.
- minNeighbors helps control detection strictness.

---

## scaleFactor

The `scaleFactor` parameter controls how much the detection window size increases after each scan.

Example:

```python
scaleFactor = 1.1
```

Meaning:

```text
100% Current Size
+
10% Increase
=
110% New Size
```

Smaller values:

- More accurate detection
- Slower processing

Larger values:

- Faster processing
- May miss some faces

Typical value:

```python
1.1
```

---

## Real-Time Face Detection

Face detection can be performed on webcam frames instead of static images.

OpenCV accesses a webcam using:

```python
camera = cv2.VideoCapture(0)
```

A frame is captured using:

```python
success, frame = camera.read()
```

Workflow:

```text
Webcam
↓
Capture Frame
↓
Convert To Grayscale
↓
Detect Face
↓
Draw Rectangle
↓
Display Frame
```

The process continues until the program is stopped.

---

## Frame

A frame is a single image captured from a webcam or video stream.

Example:

```python
success, frame = camera.read()
```

Returns:

- success -> indicates whether frame capture succeeded
- frame -> captured image

A video is made up of multiple frames displayed rapidly.

```text
Frame 1
↓
Frame 2
↓
Frame 3
↓
Frame 4
↓
Video Stream
```

Frames can be processed just like images.

---

## Key Takeaways

- Face Detection locates faces but does not identify people.
- Haar Cascade is a pre-trained face detection model.
- Grayscale images improve detection performance.
- detectMultiScale() scans images at multiple sizes.
- scaleFactor controls search window size growth.
- minNeighbors controls detector strictness.
- Face detection returns face coordinates.
- False positives can occur.
- Frames are images captured from a webcam or video stream.
- Real-time face detection processes frames continuously.