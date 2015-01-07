#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import cv2
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-c', "--cascade", required=True, help="Input path to cascade file.")

args = parser.parse_args()

cap = cv2.VideoCapture(0)

faceCascade = cv2.CascadeClassifier(args.cascade)

while(1):
    _, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags = cv2.cv.CV_HAAR_SCALE_IMAGE
    )

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    cv2.imshow('frame', frame)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
