#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import cv2
import argparse

class FaceDetector(object):

    def __init__(self, head_cascade_path, eye_cascade_path, debug=False):

        self.face_cascade = cv2.CascadeClassifier(head_cascade_path)
        self.eye_cascade = cv2.CascadeClassifier(eye_cascade_path)
        self.debug =debug
        self.cap = cv2.VideoCapture(0)

    def get_frame(self):
        _, self.frame = self.cap.read()
        return self.frame

    def get_faces(self):
        self.gray = cv2.cvtColor(self.frame, cv2.COLOR_BGR2GRAY)
        self.faces = self.face_cascade.detectMultiScale(self.gray, 1.3, 5)
        return self.faces

    def get_eyes(self):
        self.eyes = {}
        for (x, y, w, h) in self.faces:
            face = (x, y, w, h)
            roi_gray = self.gray[y : y + h, x : x + w]
            self.roi_color = self.frame[y : y + h, x : x + w]
            self.eyes[face] = self.eye_cascade.detectMultiScale(roi_gray)
        return self.eyes

    def show_debug(self):
        for (x, y, w, h) in self.faces:
            face = (x, y, w, h)
            for (ex, ey, ew, eh) in self.eyes[face]:
                cv2.rectangle(self.roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)
            cv2.rectangle(self.frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        cv2.imshow('frame', self.frame)

    def update(self):
        self.get_frame()
        self.get_faces()
        self.get_eyes()
        if self.debug:
            self.show_debug()

        return (self.faces, self.eyes)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-hc', "--head_cascade", required=True, help="Input path to head cascade file.")
    parser.add_argument('-ec', "--eye_cascade", required=True, help="Input path to eye cascade file.")
    parser.add_argument('-d', "--debug", action="store_true", help="Debug mode")

    args = parser.parse_args()

    face_detector = FaceDetector(args.head_cascade, args.eye_cascade, args.debug)

    while(1):
        face_detector.update()
        k = cv2.waitKey(5) & 0xFF
        if k == 27:
            break
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
