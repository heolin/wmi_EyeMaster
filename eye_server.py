#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import cv2

import argparse

import face_detect
import frame_processor
import input_handle
import message_server


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--port', help="Port for application server")
    parser.add_argument('-d', "--debug", action="store_true", help="Debug mode")
    parser.add_argument('-hc', "--head_cascade", required=True, help="Input path to head cascade file.")
    parser.add_argument('-ec', "--eye_cascade", required=True, help="Input path to eye cascade file.")

    args = parser.parse_args()

    face_detector = face_detect.FaceDetector(args.head_cascade, args.eye_cascade, args.debug)

    while(1):
        faces, eyes = face_detector.update()

        k = cv2.waitKey(5) & 0xFF
        if k == 27:
            break
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
