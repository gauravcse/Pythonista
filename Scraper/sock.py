import socket
sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.connect(("www.pythonlearn.com",80))
sock.send(b"GET http://lcm.csa.iisc.ernet.in/gametheory/index.html HTTP/1.0\n\n")
data=sock.recv(1500)
if data!=b"" :
    print(data)
sock.close()

