# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )
import SocketServer
from SocketServer import StreamRequestHandler as SRH
from time import ctime
import time,os,socket
serverName="RhinoServer"
Version=1.0
connections=[]

class Servers(SRH):
    name="noname"
    password=""
    def handle(self):
        connections.append(self);
        print 'got connection from ',self.client_address
        while True:
            data=""
            try:
                data = self.request.recv(1024)
            except:
                print self.name," is leav!"
                #not work
            if not data:
                print self.name," is leav!"
                loginMsg=('<%s> %s:%s at %s was leaved the chat room!' % (self.name,self.client_address[0],self.client_address[1],ctime()))
                self.broadcastMesg(loginMsg)
                connections.remove (self);
                break
            if self.name!="noname":
                print "-->>from: ", self.name
            else:
                print "-->>from: ", self.client_address
            print data
            if data!="" and data!=None:
                ds=data.split("|")
                if ds.count>1:
                    if ds[0]=="say":
                        self.broadcastMesg(self.name+":"+ds[1])
                    elif ds[0]=="regist":
                        self.name=ds[1]
                        loginMsg=('wellcome  <%s> %s:%s at %s add chat room!' % (self.name,self.client_address[0],self.client_address[1],ctime()))
                        self.broadcastMesg(loginMsg)

    def getName(self):
        self.sendMesge((self.name+":"+self.password))

    def sendFile(self,filePath):
        #print "sendFile"
        if os.path.isfile(filePath):
            self.request.send(DATA_FILE_START)
            f=open(filePath,"rb")
            self.request.send(f.read())
            f.close()
            time.sleep(0.5)
            self.request.send(DATA_FILE_END)
            return True
        else:
            self.sendError("file is not exit!")
            return False

    def broadcastMesg(self,msg):
        print ("broadcastMesg: ",msg)
        for s in connections:
            try:
                s.request.send(msg)
            except Exception as e:
                print "lost men:",e

if __name__ == '__main__':
    print serverName," ",Version," initialization is starting....."
    # host = "192.168.31.141"
    # if socket.gethostname()=="fengx-PC":
    #     host = "192.168.31.141"
    # else:
    #     host = "192.168.0.140"
    host=""
    port = 9999
    addr = (host,port)
    if len(sys.argv)>1:
        if sys.argv[1]!="":
            host= sys.argv[1]
            print sys.argv[1]
    if host=="":
        host= socket.gethostbyname(socket.gethostname())
    server = SocketServer.ThreadingTCPServer(addr,Servers)
    print serverName,' is servering on addr:',host,'port:',port
    server.serve_forever()
