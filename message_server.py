#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import zmq
import argparse

class MessageServer(object):

    def __init__(self, port):
        self.context = zmq.Context()
        self.sock = context.socket(zmq.PUB)
        self.sock.bind('tcp://*:' + str(port))

    def send(self, message):
        sock.send(message)

    def recieve(self):
        response = sock.recv()
        return response

