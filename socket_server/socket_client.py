import socket,os,time,sys
from _core import*
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
class Client():  
    #setFontColor(FONT_COLOR_DEFLUT)
    setFontColor(FONT_COLOR_DARKGREEN)
    print ">>fengx client"
    #HOST="127.0.1.1"
    HOST='localhost'
    if HOST=="":
        #print "localhost"
        HOST='localhost'
    #HOST="192.168.56.101"
    PORT=9999
    def __init__(self,host,port):
        self.HOST=host
        self.PORT=port
        
        ADDR=(self.HOST,self.PORT)
            
        self.TCP_Sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.TCP_Sock.connect(ADDR)
        
        name=""
        
        print ">>conect to : ",self.HOST,":",self.PORT
        print self.TCP_Sock.recv(1024)
        self.run()
    def run(self): 
        while True:
            setFontColor(FONT_COLOR_DEFLUT)
            data=raw_input("")
            if data!="" and data!=None:
                dataSplite=data.split()
                goodCMD=False
                recvDataType="MESAGE"
                if dataSplite[0]=="getFile":
                    filePath=""
                    outFilePath="temp"
                    if len(dataSplite)==1:
                        setFontColor(FONT_COLOR_DARKRED)
                        print "get file from server! 2 values need !   getFile <filePath> <outFilePath>"
                        setFontColor(FONT_COLOR_DEFLUT)
                    elif len(dataSplite)==2:
                        if os.path.isfile(dataSplite[1]):
                            setFontColor(FONT_COLOR_DARKRED)
                            print "there is  a  same name file!"
                            setFontColor(FONT_COLOR_DEFLUT)
                        else:
                            filePath=dataSplite[1]
                            outFilePath=dataSplite[1]
                            recvDataType="FILE"
                            goodCMD=True
                    elif len(dataSplite)==3:
                        if os.path.isfile(dataSplite[2]):
                            setFontColor(FONT_COLOR_DARKRED)
                            print "there is  a  same name file!"
                            setFontColor(FONT_COLOR_DEFLUT)
                        else:
                            filePath=dataSplite[1]
                            outFilePath=dataSplite[2]
                            recvDataType="FILE"
                            goodCMD=True
                    else:
                        print "input too more values! only 2 enough.  getFile <filePath> <outFilePath>"
                elif dataSplite[0]=="regist":
                    if len(dataSplite)==1 and data=="regist":
                        print ">>input your name and password"
                        self.regist()
                    else: print ("input too more values! : regist")
                elif dataSplite[0]=="exit()" and data=="exit()": sys.exit()
                else:
                    recvDataType="COMAND"
                    goodCMD=True
                    
                if goodCMD:
                    self.TCP_Sock.sendall(data)
                    if recvDataType=="COMAND":
                        print self.getMesage()
                    elif recvDataType=="FILE":
                        print self.getFile(outFilePath)
                    setFontColor(FONT_COLOR_DEFLUT)
            else:()
    
    def getMesage(self):
        data_start=self.TCP_Sock.recv(15)
        msg=""
        if data_start==ERROR_START:
            setFontColor(FONT_COLOR_DARKRED)
            msg=">>Error: "
            while True:
                data_mid=self.TCP_Sock.recv(1024)
                if data_mid==ERROR_END:break
                msg+=data_mid
            return msg
        elif data_start==DATA_MSG_START:
            setFontColor(FONT_COLOR_DARKGREEN)
            msg=">>"
            while True:
                data_mid=self.TCP_Sock.recv(1024)
                if data_mid==DATA_MSG_END:break
                msg+=data_mid
            return msg
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

def test():
    ips=["10.240.120.1",
    "10.240.120.15",
    "10.240.120.17 ",
    "10.240.120.22",
    "10.240.120.25"]
    
    bs=["10.240.120.34",
    "10.240.120.45",
    "10.240.120.47",
    "10.240.120.49",
    "10.240.120.60",
    "10.240.120.61",
    "10.240.120.69",
    "10.240.120.90",
    "10.240.120.101",
    "10.240.120.103",
    "10.240.120.108",
    "10.240.120.110",
    "10.240.120.113",
    "10.240.120.114",
    "10.240.120.124",
    "10.240.120.141",
    "10.240.120.149",
    "10.240.120.154",
    "10.240.120.161",
    "10.240.120.162",
    "10.240.120.164",
    "10.240.120.166",
    "10.240.120.171",
    "10.240.120.176",
    "10.240.120.180",
    "10.240.120.183",
    "10.240.120.189",
    "10.240.120.191",
    "10.240.120.194",
    "10.240.120.210",
    "10.240.120.213",
    "10.240.120.214",
    "10.240.120.217",
    "10.240.120.231",
    "10.240.120.232",
    "10.240.120.234",
    "10.240.120.235",
    "10.240.120.238",
    "10.240.120.250",
    "10.240.120.254",
    "10.240.120.255",
    "10.240.121.6",
    "10.240.121.10",
    "10.240.121.23",
    "10.240.121.24",
    "10.240.121.45",
    "10.240.121.55",
    "10.240.121.80",
    "10.240.121.81",
    "10.240.121.94",
    "10.240.121.100",
    "10.240.121.114",
    "10.240.121.134",
    "10.240.121.138",
    "10.240.121.153",
    "10.240.121.162",
    "10.240.121.173",
    "10.240.121.175",
    "10.240.121.189",
    "10.240.121.208",
    "10.240.121.210",
    "10.240.121.212",
    "10.240.121.221",
    "10.240.121.236",
    "10.240.121.246",
    "10.240.121.247",
    "10.240.121.254",
    "10.240.122.1",
    "10.240.122.3",
    "10.240.122.7",
    "10.240.122.8",
    "10.240.122.13",
    "10.240.122.14",
    "10.240.122.20",
    "10.240.122.22",
    "10.240.122.32",
    "10.240.126.2",
    "10.240.126.6",
    "10.240.126.8",
    "10.240.126.10",
    "10.240.126.11",
    "10.240.127.255"]
    for host in ips:
        port=80
        a=Client(host,port)
        print host
if __name__ == '__main__':
    test()
    #a=Client("localhost",9999)
    # host=raw_input(">>conect IP adr:")
    # port=raw_input(">>conect port adr:")
    # if port!="" :
        # port =int(port)
    # else: port =9999
    # if host!="" :
        
        # a=Client(host,port)
    # else:
        # a=Client("localhost",9999)
                