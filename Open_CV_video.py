# not work correctly
# import sys
import cv2
# import numpy as np
from typing import Any


print(cv2.__version__)
# pre-trained car detection
cascade_path = '_PATH_'
car_cascade = cv2.CascadeClassifier(cascade_path)

bbox = None
tracking = False


def mouse_callback(event: int, x: int, y: int, flags: int, param: Any):
    global bbox, tracking

    if event == cv2.EVENT_LBUTTONDOWN:
        bbox = (x, y, 0, 0)
        tracking = True

    elif event == cv2.EVENT_LBUTTONUP:
        bbox = (bbox[0], bbox[1], x - bbox[0], y - bbox[1])
        tracking = False


# Open file
video_capture = cv2.VideoCapture('test_image.mp4')

# Reading first frame
# Not fully understand
ret, frame = video_capture.read()

# Tracking objects
tracker = cv2.TrackerKCF_create()


while True:
    # Reading frame
    ret, frame = video_capture.read()

    # If tracking mode is enabled, update tracker
    if tracking:
        success = tracker.init(frame, bbox)
        tracking = False

    # Detection of cars
    cars = car_cascade.detectMultiScale(frame, scaleFactor=1.1, minNeighbors=3)

    # Object tracking
    success, bbox = tracker.update(frame)
    if not success:
        continue

    # Draw a frame around tracked object
    # ___need_rewrite!
    if success:
        bbox = tuple(map(int, bbox))
        if bbox[2] == 0 or bbox[3] == 0:
            continue
        frame = cv2.rectangle(frame, (bbox[0], bbox[1]), (bbox[0] + bbox[2], bbox[1] + bbox[3]), (0, 255, 0), 2)

        tracker = cv2.TrackerKCF_create()
        tracker.setSigma(1.5)

    # Frame display
    cv2.imshow('Video', frame)

    # Exit loop when pressing 'q' key
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()
