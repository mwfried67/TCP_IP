#!/usr/bin/env python

import socket
import time


TCP_IP = '192.168.1.112' #This is the name of the CLIENT. Not this computer.
TCP_PORT = 5005
BUFFER_SIZE = 1024
MESSAGE = "Hello, World1!"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
s.send(MESSAGE)
data = s.recv(BUFFER_SIZE)
s.close()
print "received data1:", data
time.sleep(5)

MESSAGE = "Hello, World2!"
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
s.send(MESSAGE)
data = s.recv(BUFFER_SIZE)
s.close()

print "received data2:", data
