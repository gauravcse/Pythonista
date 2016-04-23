import socket
from time import sleep
sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.connect(("www.py4inf.com",80))
sock.send("GET http://www.py4inf.com/cover.jpg HTTP/1.0\n\n")
picture=""
while True :
    data=sock.recv(1000)
    sleep(0.05)
    if(len(data)<1) :
        break
    picture=picture+data
    print '{}\t{}'.format(len(picture),len(data))
sock.close()
pos = picture.find("\r\n\r\n")
f=open('myimage3.jpg','wb')
f.write(picture[pos+4:])
f.close()
