# Day 3 - Face Recognition

## Overview

Day 3 focused on understanding the foundations of Face Recognition and building the first practical components required for a future Face Recognition Attendance System.

Unlike Day 2, which concentrated on detecting whether a face exists, Day 3 concentrated on understanding how a computer can determine whose face it is.

---

# Module 1 - Face Detection vs Face Recognition

## Face Detection

Answers:

```text
Is there a face?
```

Example:

```text
Face Found ✅
```

The detector only finds the location of the face.

Output:

```text
x
y
w
h
```

---

## Face Recognition

Answers:

```text
Whose face is this?
```

Example:

```text
Officer: Jegathayini ✅
```

Recognition identifies the person.

---

# Module 2 - Face Embeddings

A face recognition system does not compare images directly.

Instead, it converts a face into numbers.

Example:

```text
Face
↓
[0.21, -0.45, 0.88, ...]
```

This numerical representation is called a:

```text
Face Embedding
```

or

```text
Face Encoding
```

---

## Why Embeddings?

Different photos of the same person may have:

```text
Different Lighting

Different Distance

Different Camera

Different Background
```

Comparing images directly is unreliable.

Therefore:

```text
Image
↓
Embedding
↓
Comparison
```

---

## Simple Definition

A face embedding is the mathematical fingerprint of a face.

---

# Module 3 - Recognition Models

Several technologies can generate and compare embeddings.

Examples:

```text
dlib

face_recognition

MediaPipe

ArcFace
```

All follow the same basic workflow:

```text
Face
↓
Embedding
↓
Comparison
↓
Recognition
```

---

# Module 4 - Face Distance

Face recognition compares embeddings.

Example:

```text
Embedding A

[0.11, 0.52, -0.80]
```

```text
Embedding B

[0.12, 0.53, -0.79]
```

Very similar.

Result:

```text
Same Person ✅
```

---

Example:

```text
Embedding A

[0.11, 0.52, -0.80]
```

```text
Embedding C

[8.50, -4.12, 9.80]
```

Very different.

Result:

```text
Different Person ❌
```

---

# Module 5 - Known Faces Database

A recognition system must have known faces to compare against.

Example:

```text
Known_Faces/

├── Employee_A.jpg
├── Employee_B.jpg
├── Employee_C.jpg
```

Workflow:

```text
Known Face
↓
Generate Embedding
↓
Store Embedding
↓
Future Comparison
```

---

# Practical 1 - Face Detection On A Known Face

Goal:

```text
Load Image
↓
Detect Face
↓
Draw Rectangle
```

Tools Used:

```text
OpenCV

Haar Cascade
```

Concepts Learned:

```text
detectMultiScale()

x

y

w

h
```

---

# Coordinates Used In Face Detection

Top Left:

```text
(x, y)
```

Top Right:

```text
(x + w, y)
```

Bottom Left:

```text
(x, y + h)
```

Bottom Right:

```text
(x + w, y + h)
```

---

# Practical 2 - ROI (Region Of Interest)

ROI means:

```text
Region Of Interest
```

In Face Recognition:

```text
The Face
```

is the ROI.

---

## Face Cropping

Code Concept:

```python
face_roi = img[
    y:y+h,
    x:x+w
]
```

Meaning:

```text
Extract only the face area.
```

---

## Why ROI Is Important

Instead of processing:

```text
Wall

Chair

Background

Face
```

we process:

```text
Face Only
```

which improves recognition.

---

# Practical 3 - Saving The Cropped Face

Concept:

```python
cv2.imwrite()
```

Used To:

```text
Save Image To Storage
```

Example:

```python
cv2.imwrite(
    "cropped_face.jpg",
    face_roi
)
```

---

## Difference Between imread and imwrite

### cv2.imread()

```text
Read image from storage into memory.
```

### cv2.imwrite()

```text
Save image from memory into storage.
```

---

# Practical 4 - Multiple Face Processing

Goal:

```text
Detect Multiple Faces
↓
Crop Each Face
↓
Save Each Face
```

Example Output:

```text
face_1.jpg

face_2.jpg

face_3.jpg
```

---

## Counter Variable

```python
face_count += 1
```

Meaning:

```python
face_count = face_count + 1
```

Example:

```text
1
↓
2
↓
3
↓
4
```

---

# Practical 5 - Face Labeling

Text was added above detected faces.

Example:

```python
cv2.putText()
```

Output:

```text
Face Found
```

displayed above the rectangle.

---

## Font Used

```python
cv2.FONT_HERSHEY_SIMPLEX
```

Meaning:

```text
A built-in OpenCV font style.
```

---

# Complete Recognition Pipeline

By the end of Day 3, the complete recognition workflow was understood:

```text
Image
↓
Face Detection
↓
Face ROI
↓
Face Embedding
↓
Embedding Comparison
↓
Recognition
```

---

# Key Terms Learned

```text
Face Detection

Face Recognition

Face Embedding

