from __future__ import print_function
from imutils.object_detection import non_max_suppression
# non_max_suppression takes multiple, overlapping bounding boxese
# and reduces them to a single bounding box
from imutils import paths
import numpy as np
import argparse
import imutils
import cv2
import time

# argument parse constructor and application
ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video",
    help = "path to the (optional) video file")
args = vars(ap.parse_args())

# handles where the computer gets video from
if not args.get("video", False):
    camera = cv2.VideoCapture(0) #live video from macbook camera
else:
    camera = cv2.VideoCapture(args["video"]) #given video

# sets up HOGDescriptor
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())


while True:
    (grabbed, frame) = camera.read()

    if args.get("video") and not grabbed:
        break

    frame = imutils.resize(frame, width = 200) #find a value between 200 and 800 (?) that is large enough but the video doesnt slow down

    (rects, weights) = hog.detectMultiScale(frame, winStride = (4, 4),
        padding = (8, 8), scale = 1.05)
    frameClone = frame.copy()

    rects = np.array([[x, y, x + w, y + h] for (x, y, w, h) in rects])
    pick = non_max_suppression(rects, probs = None, overlapThresh = 0.65)

    for (xA, yA, xB, yB) in pick:
        cv2.rectangle(frameClone, (xA, yA), (xB, yB), (0, 255, 0), 2)

    cv2.imshow("Pedestrian", frameClone)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

camera.release()
cv2.destroyAllWindows()

# also in use: scripttrack.py and detect_character.py and detect_pedestrians.py
