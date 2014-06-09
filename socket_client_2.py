#!/usr/bin/env python
import  socket
import wx
import  time 

HOST="localhost"
PORT=56219


s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.connect((HOST,PORT))
print s.recv(8096)
while 1:
        
        while True:
                data=raw_input("conmand: ")
                if not data:
                        break
                else:
                        s.send(data)
                        recv=s.recv(4096)
                        print recv
s.close()