import socket
def print_machine_info() :
    host=socket.gethostname()
    ip=socket.gethostbyname(host)
    print '{}   {}'.format("HOST NAME :",host)
    print '{}   {}'.format("IP ADDRESS :",ip)
if __name__=='__main__' :
    print_machine_info()

