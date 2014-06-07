from socket import *
import thread
import select
PORT=5648
BUFSIZE=1024


ADDR=("",PORT)
tcpSerSock=socket(AF_INET,SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)


def th():
        #global tcpCliSock
        while True:
                data=raw_input("")
                if not data:
                        break
                tcpSerSock.send(data)
#tcpSerSock.setblocking(0)
print "waiting fot connection..."

while True:
        infds,outfds,errfds = select.select([tcpSerSock,],[],[],5) 
        
        clientsock,clientaddr = tcpSerSock.accept()
        infds_c,outfds_c,errfds_c = select.select([clientsock,],[],[],3)
        if len(infds) != 0: 
                if len(infds_c) != 0: 
                    buf = clientsock.recv(1024) 
                    if len(buf) != 0: 
                        print (buf)
                #clientsock.close()
                print "clientsock closed"
        print "no data coming"

try:
        #tcpSerSock,addr=tcpSerSock.accept()
        print "connection from :%s" % str(addr)


except:
        print "connect fath!"
#thread.start_new_thread(th,())

        '''
        data=tcpSerSock.recv(BUFSIZE)
        if not data:
                        break
        print data
        tcpSerSock.send("xxxxcc")
        if str(data)=="shot down server":
                        tcpSerSock.close()

        #client,ipaddr=s.accept()
        #client.send("echo:")
        #print "Got a connect from %s"  %str(ipaddr)
        data=client.recv(1024)
        print "receive data:%s" %data
        client.send("echo:"+data)
        client.close()
        '''