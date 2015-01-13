#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import zmq
import argparse
import numpy as np
from operator import attrgetter

class FrameProcessor:
    def get_eye_angle(eyes):
        return None

    def get_head_angle(self, faces, eyes, noses):
        for (x, y, w, h) in faces:
            face = (x, y, w, h)
            if len(noses) > 0:
                nose = (noses[face][0][0], noses[face][0][1],\
                        noses[face][0][2], noses[face][0][2])
                eyes = [(eye[0], eye[1], eye[2], eye[3]) for eye in eyes[face]]

                if eyes[0][0] > eyes[1][0]:
                    left_eye = eyes[0]
                    right_eye = eyes[1]
                else:
                    left_eye = eyes[1]
                    right_eye = eyes[0]

                left_eye_center = left_eye[0] + left_eye[2]
                right_eye_center = right_eye[0] + right_eye[2]
                nose_center = nose[0] + nose[2]

                result = (right_eye_center - left_eye_center)/2 - nose_center
                print result
            return result

        return None
