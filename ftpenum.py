#!/usr/bin/python
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("192.168.0.13",21))
resp = s.recv(1024)
print resp

s.send("USER anonymous\r\n")
r = s.recv(1024)
print r

s.send("PASS anonymous\r\n")
r = s.recv(1024)
print r

s.send("PWD \r\n")
s.send("QUIT \r\n")
r = s.recv(2048)
print r
