# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )
import socket,os,time,sys,wx
from _core import*
from threading import Thread
from wx.lib.pubsub import pub
# FONT_COLOR_RED=12
# FONT_COLOR_DARKRED=4
# FONT_COLOR_BLUE=9
# FONT_COLOR_DARKBLUE=1
# FONT_COLOR_GREEN=10
# FONT_COLOR_DARKGREEN=2
# FONT_COLOR_WHITE=15
# FONT_COLOR_GRAY=8
# FONT_COLOR_YELLOW=14
# FONT_COLOR_DARKYELLOW=6
# FONT_COLOR_DEFLUT=FONT_COLOR_WHITE
#def runClient():

class chatClient():
    #setFontColor(FONT_COLOR_DEFLUT)
    setFontColor(FONT_COLOR_DARKGREEN)
    HOST='localhost'
    HOST='192.168.0.99'
    if HOST=="":
        HOST='localhost'
    PORT=9999
    def __init__(self,host,port):
        self.HOST=host
        self.PORT=port
        ADDR=(self.HOST,self.PORT)
        self.TCP_Sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.TCP_Sock.connect(ADDR)
        name=""
        print ">>conect to : ",self.HOST,":",self.PORT
        #print self.TCP_Sock.recv(1024)

class Client():
    setFontColor(FONT_COLOR_DARKGREEN)
    HOST='localhost'
    if HOST=="":
        HOST='localhost'
    PORT=9999
    def __init__(self,host,port):
        self.HOST=host
        self.PORT=port
        ADDR=(self.HOST,self.PORT)
        self.TCP_Sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.TCP_Sock.connect(ADDR)
        name=""
        print ">>conect to : ",self.HOST,":",self.PORT
        #print self.TCP_Sock.recv(1024)
        #self.run()
        pub.subscribe(self.sendMsgToServer, "sendMsgToServer")

    def run(self):
        while True:
            data=self.TCP_Sock.recv(1024)
            if data!="" and data!=None:
                wx.CallAfter(pub.sendMessage , "recvMsgToServer", m=data)
            setFontColor(FONT_COLOR_DEFLUT)

    def getFile(self,outFilePath):
        data_start=self.TCP_Sock.recv(15)
        msg=""
        if data_start==DATA_FILE_START:
            setFontColor(FONT_COLOR_DARKGREEN)
            #msg+="start get file ",filePath," data..."
            newFile=open(outFilePath,"wb")
            while True:
                data_mid=self.TCP_Sock.recv(1024)
                if data_mid==DATA_FILE_END:
                    #msg+= "getFile: ",dataSplite[1],"complite"
                    newFile.close()
                    break
                newFile.write(data_mid)
            msg=">>get file complite"

        elif data_start==ERROR_START:
            setFontColor(FONT_COLOR_DARKRED)
            msg=">>Error: "
            while True:
                data_mid=self.TCP_Sock.recv(1024)
                if data_mid==ERROR_END:break
                msg+=data_mid
        return msg
    def regist (self):
        self.TCP_Sock.sendall("regist")
        setFontColor(FONT_COLOR_YELLOW)
        self.name=raw_input("name:")

        self.TCP_Sock.send(self.name)
        password=raw_input("password:")
        self.TCP_Sock.send(password)
        print self.getMesage()
        setFontColor(FONT_COLOR_DEFLUT)
    def sendMsgToServer(self,msg):
        t=msg
        self.TCP_Sock.send(t)
        print "send:",t

class ClientChread(Thread):
    host = "192.168.0.140"
    host = "192.168.31.141"
    host= socket.gethostbyname(socket.gethostname())
    client=Client(host,9999)
    def __init__(self):
        Thread.__init__(self)
        self.start()
    def run(self):
        self.client.run()

if __name__ == '__main__':
    host = "192.168.31.141"
    if socket.gethostname()=="fengx-PC":
        host = "192.168.31.141"
    else:
        host = "192.168.0.140"
    a=Client(host,9999)
