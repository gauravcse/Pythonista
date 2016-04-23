import socket

host = 'localhost'        # Symbolic name meaning all available interfaces
port = 12345     # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(5)
conn, addr = s.accept()
print('Connected by', addr)
while True:
    data = conn.recv(2048)
    if not data: break
    conn.sendall(data)
conn.close()
