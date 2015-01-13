#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import zmq
import argparse
from operator import attrgetter

class FrameProcessor:
    def get_eye_angle(eyes):
        return None

    def get_head_angle(self, faces, eyes, noses):
        if len(noses) > 0:
            print(str(noses[0]))
            nose = min(noses, key=attrgetter('ey'))
            left_eye = min(eyes, key=attrgetter('ex'))
            right_eye = max(eyes, key=attrgetter('ex'))

            left_eye_center = left_eye.ex + left_eye.ew
            right_eye_center = right_eye.ex + right_eye.ew
            nose_center = nose.ex + nose.ew

            result = (right_eye_center - left_eye_center)/2 - nose_center
            print(str(result))
            return result

        return None
