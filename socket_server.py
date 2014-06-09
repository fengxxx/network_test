#!/usr/bin/env python
import  socket
import os
import time 
HOST="localhost"
PORT=56219

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((HOST,PORT))
s.listen(3)

c,addr=s.accept()
print "connected by: ",addr

c.sendall("connected success!")    	
while 1:
        data=c.recv(4096)
        print data
        if not data:
        		#break
        		time.sleep(1.5)
    	        cmd =os.popen(data)

     	
        result=cmd.read()
        print result
        c.send(result)




        if data=="111":
                print "close!!!!"
            	s.close()
  	            	
