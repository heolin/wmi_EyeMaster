#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import cv2
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-hc', "--head_cascade", required=True, help="Input path to head cascade file.")
parser.add_argument('-ec', "--eye_cascade", required=True, help="Input path to eye cascade file.")

args = parser.parse_args()

cap = cv2.VideoCapture(0)

face_cascade = cv2.CascadeClassifier(args.head_cascade)
eye_cascade = cv2.CascadeClassifier(args.eye_cascade)

while(1):
    _, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        roi_gray = gray[y : y + h, x : x + w]
        roi_color = frame[y : y + h, x : x + w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

    cv2.imshow('frame', frame)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
