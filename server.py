#!/usr/bin/env python

import socket
import argparse

parser = argparse.ArgumentParser(description='Server receiving connections')
parser.add_argument('--port', default=12345, required=False,
                    dest='port', help='Port to listen')
parser.add_argument('--buffer', default=20, required=False,
                    dest='buffer', help='Buffer to be used')
parser.add_argument('--bind_adr', default='127.0.0.1', required=False,
                    dest='bind_adr', help='Bind address to be used')
args = parser.parse_args()

TCP_IP = args.bind_adr
TCP_PORT = args.port
BUFFER_SIZE = args.buffer  # Normally 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)

conn, addr = s.accept()
print 'Connection address:', addr
while 1:
    data = conn.recv(BUFFER_SIZE)
    if not data: break
    print "received data:", data
    conn.send(data)  # echo
conn.close()