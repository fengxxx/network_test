#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import socket
import select

host = "127.0.0.1" #"" 
port = 53591
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 
s.bind((host,port)) 
s.listen(5)
print "begin..."
while 1: 
    infds,outfds,errfds = select.select([s,],[],[],5) 
    # 如果infds状态改变,进行处理,否则不予理会 
    if len(infds) != 0: 
        clientsock,clientaddr = s.accept()
        infds_c,outfds_c,errfds_c = select.select([clientsock,],[],[],3)
        if len(infds_c) != 0: 
            buf = clientsock.recv(1024) 
            if len(buf) != 0: 
                print (buf)
        clientsock.close()
        print "clientsock closed"
    print "no data coming"