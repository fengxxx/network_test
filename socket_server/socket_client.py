import socket 
import time 

SERVER_NAME=" SERVER_01"
SERVER_NAME=" server_02"
#HOST="127.0.0.1"
HOST='localhost'

PORT=9999

BUFSIZE=1024
ADDR=(HOST,PORT)
TCP_Sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
TCP_Sock.connect(ADDR)
print TCP_Sock.recv(1024)

if __name__ == '__main__':
    while True:
        data=raw_input("")
        if data!="" and data!=None:
            TCP_Sock.sendall(data)
            startRecvFile=False
            if data.split()[0]=="getFile":
                print "start get file data..."
                f=open(data.split()[2],"wb")
                while True:
                    print "get data..."
                    fdata=TCP_Sock.recv(1024)
                    #print "rev: ",fdata
                    if fdata=="send complite":
                        print "get complite "
                        f.close()
                        break
                    if startRecvFile: f.write(fdata)
                    if fdata=="send start":
                        print "get start "
                        startRecvFile=True
            else:
                msg=""
                data_start=TCP_Sock.recv(10)
                if data_start=="data_start":
                    while True:
                        data_mid=TCP_Sock.recv(1024)
                        if data_mid=="data_end":break
                        msg+=data_mid
                    print msg
        else:()
