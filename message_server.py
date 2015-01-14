#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import zmq
import argparse

class MessageServer(object):

    def __init__(self, port):

        self.port = "8080"
        if port:
            self.port = port
        self.context = zmq.Context()
        self.sock = self.context.socket(zmq.PUB)
        self.sock.bind('tcp://*:8080')#'tcp://*:' + str(self.port))

    def send(self, message):
        self.sock.send(message)

    def recieve(self):
        response = sock.recv()
        return response

