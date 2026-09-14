import cv2
# Bring OpenCV library into this program.

import mediapipe as mp
# Bring MediaPipe library into this program.

mp_face_detection = mp.solutions.face_detection

face_detector = mp_face_detection.FaceDetection(
    model_selection=0,
    min_detection_confidence=0.5
)
# Load MediaPipe face detector.

camera = cv2.VideoCapture(0)
# Open webcam.


while True:

    success, frame = camera.read()
    # Capture frame.

    rgb_frame = cv2.cvtColor(
        frame,
        cv2.COLOR_BGR2RGB
    )
    # Convert BGR to RGB.

    results = face_detector.process(
        rgb_frame
    )
    # Detect faces using MediaPipe.


    if results.detections:

        for detection in results.detections:

            bbox = detection.location_data.relative_bounding_box

            frame_height, frame_width, _ = frame.shape

            x = int(bbox.xmin * frame_width)
            y = int(bbox.ymin * frame_height)

            w = int(bbox.width * frame_width)
            h = int(bbox.height * frame_height)

        cv2.rectangle(
            frame,
            (x, y),
            (x + w, y + h),
            (0, 255, 0),
            3
        )

        face_roi = frame[
            y:y+h,
            x:x+w
        ]
        # Extract face region.

        cv2.imshow(
            "Face ROI",
            face_roi
        )
        # Display cropped face.

    cv2.imshow(
        "Webcam Face Detection",
        frame
    )

    key = cv2.waitKey(1)

    if key == ord("q"):
        break

camera.release()

cv2.destroyAllWindows()