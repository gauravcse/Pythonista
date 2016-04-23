import socket
import sys

#hostname,backlog time and data to be recovered
host=''
backlog=5
payload=1024
port=6677
#Declaring the socket ( TCP )
sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#Enable reuse address/port
sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

#Declares Server Address
server_address=(host,port)

print "Starting up Echo Server %s at Port %s"%(server_address)
sock.bind(server_address)

sock.listen(backlog)

while True:
    print "Waiting to receive from the client"
    client,address = sock.accept()
    data=client.recv(payload)
    if(len(data)<1) :
        print "Error on the Server Side"
    print "Data : %s"%data
    client.send(data)
    #Close connection
    client.close()


        
