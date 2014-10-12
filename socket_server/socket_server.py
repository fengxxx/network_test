import SocketServer  
from SocketServer import StreamRequestHandler as SRH  
from time import ctime  
import time  
import os
host = "localhost"  
port = 9999  
addr = (host,port)  

class Servers(SRH):  
    def handle(self):  
        print 'got connection from ',self.client_address  
        self.wfile.write('connection %s:%s at %s succeed!\n %s' % (host,port,ctime(),self.client_address))  
        while True:  
            try:
                data = self.request.recv(1024)  
            except:
                print self.client_address," is leav!"
            if not data:   
                break  
            if data.split()[0]=="getFile": 
                f=open(data.split()[1],"rb")
                time.sleep(0.5)
                self.request.send("send start")
                self.request.send(f.read())
                f.close()
                time.sleep(0.5)
                self.request.send("send complite")
            else:
                msg=os.popen(data).read()
                #print msg
                self.request.send("data_start")
                #time.sleep(0.5)
                if msg=="" or msg==None: msg="'"+data+"'"+": is not recognized as an internal or external command"
                self.request.send(msg)
                time.sleep(0.5)
                self.request.send("data_end")
            print data  
            print "RECV from ", self.client_address
print 'server is running....'  
server = SocketServer.ThreadingTCPServer(addr,Servers)  
server.serve_forever()  