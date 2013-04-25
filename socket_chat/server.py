# UDP Ip chat server
from socket import *

host = "localhost"
port = 2156
buf = 1024
addr = (host, port)
UDPSock = socket(AF_INET, SOCK_DGRAM)
UDPSock.bind(addr)

while 1:

    data,addr = UDPSock.recvfrom(buf)
    if not data:

        break

    else:
        if data == 'exit':
            print "Client exitted..."
            UDPSock.close()
            break 
        print "\nReceived message :", data

    data1 = raw_input("Enter the data to be sent >> ")
    UDPSock.sendto(data1, addr)
    if data1 == 'exit':
        UDPSock.close()
        break
    print "Sending reply :", data1


