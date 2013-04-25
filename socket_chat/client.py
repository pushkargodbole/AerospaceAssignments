# UDP Ip chat client
from socket import *
import sys

host = "localhost"
port = 2156
buf = 1024
addr = (host, port)
UDPSock = socket(AF_INET, SOCK_DGRAM)


while(1):
    data = raw_input('Enter message to send to server...> ')
    if not data :
        sys.exit(1)

    else :
        if (UDPSock.sendto(data,addr)):
            if data == 'exit':
                UDPSock.close()
                break
            print "Sending message :", data

        data1, addr = UDPSock.recvfrom(buf)
        if data1 == 'exit':
            print "Server exitted..."
            UDPSock.close()
            break
        print "\nReceived message :", data1

