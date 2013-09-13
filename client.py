#!/usr/bin/env python

import socket
import argparse

parser = argparse.ArgumentParser(description='Client sending data')
parser.add_argument('--port', default=12345, required=False,
                    dest='port', help='Port to listen')
parser.add_argument('--buffer', default=1024, required=False,
                    dest='buffer', help='Buffer to be used')
parser.add_argument('--bind_adr', default='127.0.0.1', required=False,
                    dest='bind_adr', help='Bind address to be used')
parser.add_argument('--message', default='Hello World !!', required=False,
                    dest='message', help='Message to send to the server')
args = parser.parse_args()

TCP_IP = args.bind_adr
TCP_PORT = args.port
BUFFER_SIZE = args.buffer
MESSAGE = args.message

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
s.send(MESSAGE)
data = s.recv(BUFFER_SIZE)
s.close()

print "received data:", data