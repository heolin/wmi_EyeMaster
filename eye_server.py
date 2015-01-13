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
    parser.add_argument('-nc', "--nose_cascade", required=True, help="Input path to nose cascade file.")

    args = parser.parse_args()

    face_detector = face_detect.FaceDetector(args.head_cascade, args.eye_cascade, args.nose_cascade, args.debug)
    frame_process = frame_processor.FrameProcessor()
    n = 0

    while(1):
        faces, eyes, noses = face_detector.update()
        
        n += 1
        if n%10 == 0:
            frame_process.get_head_angle(faces, eyes, noses)

        k = cv2.waitKey(5) & 0xFF
        if k == 27:
            break
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
