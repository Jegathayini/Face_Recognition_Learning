# Computer Vision & Face Recognition Learning Journey

A structured, day-by-day learning repository documenting my complete journey from absolute beginner in Computer Vision to building practical Face Recognition and Attendance systems using Python.

This repository is designed for learners who want to **understand** the concepts deeply rather than just copy-paste code.

---

## Overview

This repository is a comprehensive documentation of my personal learning journey in **Computer Vision**, **Image Processing**, and **Face Recognition**.

It follows a clear and progressive learning path:

- Starting from the very basics of digital images and pixels
- Moving through OpenCV fundamentals and webcam handling
- Learning classical and modern face detection techniques
- Understanding the difference between Face Detection and Face Recognition
- Working with face embeddings and matching logic
- Building attendance system foundations
- Creating a complete mini web application using Flask + InsightFace

The repository contains:

- Clean and beginner-friendly **Notes**
- Hands-on **Exercises** organized by day
- Progressive mini-projects
- A working Flask application for employee registration using face embeddings

Everything is structured so that anyone can follow the same path and build strong fundamentals.

---

## Learning Objectives

By the end of this repository, you will be able to:

- Understand how digital images are represented (pixels, channels, resolution)
- Use OpenCV confidently for image and video processing
- Perform real-time face detection using webcam
- Extract face regions (ROI) and prepare datasets
- Understand face embeddings and how recognition actually works
- Build the core logic of a face-based attendance system
- Create a simple web interface to register faces using deep learning models

---

## Learning Roadmap

### Phase 1: Python & OpenCV Basics (Day 1)

**Topics Covered:**
- What is Computer Vision?
- What is an Image and a Pixel?
- Image Resolution
- RGB vs BGR color format in OpenCV
- Reading and displaying images
- Understanding image shape `(height, width, channels)`
- Accessing individual pixel values
- Converting images to Grayscale
- Drawing rectangles and putting text on images
- Accessing webcam and capturing frames
- Saving video streams

**Key Takeaway:**  
You learn how computers “see” images as numerical data and how to manipulate them using OpenCV.

---

### Phase 2: Face Detection (Day 2)

**Topics Covered:**
- Haar Cascade Classifiers
- Face detection on static images
- Real-time face detection from webcam
- Drawing bounding boxes around detected faces

**Key Takeaway:**  
You learn how to locate faces in an image or video stream.

---

### Phase 3: Advanced Face Handling (Day 3)

**Topics Covered:**
- Difference between Face Detection and Face Recognition
- Extracting Face ROI (Region of Interest)
- Cropping single and multiple faces
- Labeling detected faces
- Experimenting with MediaPipe

**Key Takeaway:**  
You learn how to prepare clean face data which is essential for recognition.

---

### Phase 4: Attendance System Foundations (Day 4)

**Topics Covered:**
- Creating attendance records using CSV
- Automatic date and time generation using `datetime`
- Writing and reading attendance data
- Preventing duplicate attendance entries (same person same day)
- Generating attendance summaries and reports

**Key Takeaway:**  
You learn the complete backend logic of an attendance system (without recognition yet).

---

### Phase 5: Face Recognition Concepts (Day 5)

**Topics Covered:**
- Loading known faces
- Understanding face embeddings
- Comparing faces using distance metrics
- Employee registry concepts
- Recognition logic
- Webcam-based face detection + ROI extraction
- Building basic recognition pipelines

**Key Takeaway:**  
You understand how face recognition actually works under the hood (embeddings + matching).

---

### Phase 6: Advanced Recognition Engines (Day 6)

**Topics Covered:**
- Building complete attendance engines (multiple versions)
- Loading embedders
- Creating presence detection systems (`presenx`)
- Improving recognition pipelines step by step

**Key Takeaway:**  
You start combining everything into more complete real-world systems.

---

## Repository Structure

```text
Face_Recognition_Learning/
│
├── Exercises/
│   ├── Day_1/               # OpenCV fundamentals
│   │   ├── image_read.py
│   │   ├── image_shape.py
│   │   ├── pixel_values.py
│   │   ├── grayscale.py
│   │   ├── draw_rectangle.py
│   │   ├── put_text.py
│   │   ├── webcam_basics.py
│   │   ├── save_video.py
│   │   └── ...
│   │
│   ├── Day_2/               # Face Detection
│   │   ├── face_detection_image.py
│   │   └── realtime_face_detection.py
│   │
│   ├── Day_3/               # Face ROI & Advanced Detection
│   │   ├── face_roi.py
│   │   ├── face_crop.py
│   │   ├── multiple_face_crop.py
│   │   ├── face_label.py
│   │   └── mediapipe_experiment.py
│   │
│   ├── Day_4/               # Attendance System Logic
│   │   ├── create_attendance_file.py
│   │   ├── write_attendance.py
│   │   ├── read_attendance.py
│   │   ├── auto_attendance.py
│   │   ├── check_duplicae.py
│   │   ├── attendance_summary.py
│   │   └── attendance_report.py
│   │
│   ├── Day_5/               # Recognition Foundations
│   │   ├── load_known_face.py
│   │   ├── explore_embedder.py
│   │   ├── distance_demo.py
│   │   ├── recognition_logic.py
│   │   ├── employee_registry.py
│   │   ├── webcam_face_detection.py
│   │   └── ...
│   │
│   └── Day_6/               # Advanced Engines
│       ├── attendance_engine.py
│       ├── attendance_engine_v2.py
│       ├── attendance_engine_v3.py
│       ├── attendance_engine_v4.py
│       ├── load_embedder.py
│       ├── presenx_v1.py
│       └── presenx_v2.py
│
├── Notes/
│   ├── day1_fundamentals.md
│   ├── day2_face_detection.md
│   ├── day3_face_recognition.md
│   ├── day4_attendance_system.md
│   └── day5_face_recognition_foundations.md
│
├── templates/
│   └── addemployee.html          # Frontend form for employee registration
│
├── app.py                        # Flask application (InsightFace based)
└── README.md