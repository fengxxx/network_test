#!/usr/bin/env python
import  socket

HOST="localhost"
PORT=56219

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((HOST,PORT))
s.listen(3)

c,addr=s.accept()

while 1:
	print "connected by: ",addr
	
	c.sendall("connected success!")
	c.sendall("./websocket.html")
	data=c.recv(4096)
	if not data:break
	if data=="111":
		print "close!!!!"
		
	print addr,"  send:   <",data,">"
	c.sendall(data)
	

