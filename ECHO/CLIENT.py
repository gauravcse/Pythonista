import socket
import sys
host='localhost'
port=6677

#echo client

sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_address=(host,port)
print "Connecting to the %s port %s"%(server_address)
sock.connect(server_address)

#Data Sending part

try :
    message="This is GAURAV MITRA Speaking"
    print '{} {}'.format("The message to be sent is ",message.rstrip())
    sock.sendall(message)
    amount_received=0
    amount_expected=len(message)
    while amount_received<amount_expected :
        data=sock.recv(18)
        amount_received+=len(data)
except Exception, e :
    print '{} {}'.format("exception is",str(e))
finally :
    sock.close()
    
