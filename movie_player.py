#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import argparse
import cv2
import zmq


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file', help="AVI file to play")
    parser.add_argument('-p', '--port', help="Port.")

    args = parser.parse_args()

    context = zmq.Context()
    sock = context.socket(zmq.SUB)
    sock.setsockopt(zmq.SUBSCRIBE, '')

    sock.connect('tcp://localhost:8080')

    cap = cv2.VideoCapture(args.file)

    _, frame = cap.read()
    frame_counter = 0
    while(1):

        message = sock.recv()
        if message != "None":
            _, frame = cap.read()
            frame_counter += 1
            if frame_counter == cap.get(cv2.cv.CV_CAP_PROP_FRAME_COUNT):
                frame_counter = 0
                cap.set(cv2.cv.CV_CAP_PROP_POS_FRAMES, 0)

        cv2.imshow('frame', frame)

        k = cv2.waitKey(5) & 0xFF

        if k == 27:
            break

    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
