#!/usr/bin/env python

import socket
import time
print "Got to start"
TCP_IP = '192.168.1.112' #This is the name of this computer
TCP_PORT = 5005
BUFFER_SIZE = 20  # Normally 1024, but we want fast response

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)
print "Got past listen"
conn, addr = s.accept()
print 'Connection address:', addr
while 1:
    data = conn.recv(BUFFER_SIZE)
    print "Got Here"
    if not data: time.sleep(5)
    print "received data:", data
    conn.send(data)  # echo
print "close connection"
time.sleep(1)
conn.close()
