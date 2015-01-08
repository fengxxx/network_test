import SocketServer  
from SocketServer import StreamRequestHandler as SRH  
from time import ctime  
from _core import*
import time,os


host = "localhost"  
host = "192.168.3.104"  
port = 9999  
port = 1234


class Servers(SRH):  
    name="noname"
    password=""
    def handle(self):  
        setFontColor(FONT_COLOR_DARKGREEN)
        print 'got connection from ',self.client_address  
        self.wfile.write('>>connection %s:%s at %s succeed!' % (host,self.client_address[1],ctime()))  
        setFontColor(FONT_COLOR_DEFLUT)
        while True:  
            try:
                data = self.request.recv(1024)  
            except:
                print self.client_address," is leav!"
            if not data:   
                break
                
            setFontColor(FONT_COLOR_YELLOW)
            if self.name!="noname":
                print "-->>from: ", self.name
            else: 
                print "-->>from: ", self.client_address
            setFontColor(FONT_COLOR_DEFLUT)
            print data
            if data!="" and data!=None:
                setFontColor(FONT_COLOR_DARKGREEN)
                dataSplite=data.split()
                if dataSplite[0]=="getFile":
                    filePath=""
                    if len(dataSplite)==1:
                        self.sendError("get file from server! 2 values need ! :  getFile <filePath> <outFilePath>")
                    elif len(dataSplite)==2 or len(dataSplite)==3:
                        print "sendBackFile: ",self.sendFile(dataSplite[1])
                    else:
                        print "sendBackError: ",self.sendError("input too more values! only 2 enough. : getFile <filePath> <outFilePath>")
                elif dataSplite[0]=="regist" and data=="regist":
                    if len(dataSplite)==1:
                        print ">> regist: ",self.client_address 
                        self.regist()
                    else: print "sendBackError: ",self.sendError("input too more values! : regist")
                elif dataSplite[0]=="myName" and data=="myName":
                    self.getName()
                else:
                    msg=os.popen(data).read()
                    if msg=="" or msg==None: 
                        msg="'"+data+"'"+": is not recognized as an internal or external command"
                        print "sendBackError: ",self.sendError(msg)  
                    else: print "sendMesge: ",self.sendMesge(msg)  
    def getName(self):
        self.sendMesge((self.name+":"+self.password))
    def sendMesge(self,msg):
        #print "sendMesge"
        if msg!="" and msg!=None:
            self.request.send(DATA_MSG_START)
            self.request.send(msg)
            time.sleep(0.5)
            self.request.send(DATA_MSG_END)
            return True
        else:return False
    def sendError(self,err):
        #print "sendError"
        if err!="" and err!=None:
            self.request.send(ERROR_START)
            self.request.send(err)
            time.sleep(0.5)
            self.request.send(ERROR_END)
            return True
        return False
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
    def regist(self):
        #self.sendMesge(REGIST_GIVE)
        print ">>get name: "
        self.name = self.request.recv(30)
        print ">>get password: "
        self.password=self.request.recv(30)
        print ">>regist succeed "
        self.sendMesge(("regist succeed \n>>Congratulations to you :"+self.name))

if __name__ == '__main__':
    import socket as s
    host=s.gethostbyname_ex(s.gethostname())[2][0]
    print "info: ",s.gethostbyname_ex(s.gethostname())
    print "host: ",host
    #port=raw_input(">>conect port adr:")
    #if port!="":
    #    port=int(port)
    #else:
    #    port=9999
    
    if host=="" : host="localhost"
    addr = (host,port)  
    server = SocketServer.ThreadingTCPServer(addr,Servers)  
    print 'server is running....'  
    server.serve_forever()  