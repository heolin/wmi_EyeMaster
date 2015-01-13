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
            if noses[face] is not bool and eyes[face] is not bool and len(noses[face]) > 0 and len(eyes[face]) > 1:
                print(str(noses[face]))
                nose = min(noses[face], key=lambda item:item[1])
                nose = (nose[0], nose[1],
                        nose[2], nose[2])
                eyes = [(eye[0], eye[1], eye[2], eye[3]) for eye in eyes[face]]

                left_eye = min(eyes, key=lambda item:item[0])
                right_eye = max(eyes, key=lambda item:item[0])


                left_eye_center = left_eye[0] + left_eye[2]
                right_eye_center = right_eye[0] + right_eye[2]
                nose_center = nose[0] + nose[2]

                result = (right_eye_center + left_eye_center)/2 - nose_center
                print result
                return result

        return None
