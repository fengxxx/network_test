from socket import *
import thread
#HOST='localhost'

SEND_MSG=" "

SERVER_NAME=" SCRVER_01"
HOST="127.0.0.1"
PORT=5648
#PORT=53432
BUFSIZE=1024
ADDR=(HOST,PORT)
TCP_Sock=socket(AF_INET,SOCK_STREAM)
TCP_Sock.connect(ADDR)
#TCP_Sock.setblocking(1)
print SEND_MSG
if __name__ == '__main__':	
   
     
    #SEND_MSG=TCP_Sock.recv(BUFSIZE)
    #print SEND_MSG
    while True:
    	data=raw_input("")
    	TCP_Sock.send(data)
'''
        if not SEND_MSG:
            break
        print SEND_MSG
'''
