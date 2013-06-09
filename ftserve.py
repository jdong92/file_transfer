import socket
import os

HOST = '127.0.0.1'
PORT = 9050

try:
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
except socket.error:
    print 'Failed to create socket'
    sys.exit()

s.bind((HOST, PORT))
s.listen(1)

conn, addr = s.accept()

print 'Connect by', addr

while 1:
    data = conn.recv(1024)
    data = data.split()
    if not data: break
    elif data[0] and len(data) == 1:
        files = [f for f in os.listdir('.') if os.path.isfile(f)]
        for f in files:
            print f
    elif data[0] == 'get' and len(data) == 2:
        files = [f for f in os.listdir('.') if os.path.isfile(f)]
        for f in files:
            if data[1] == f:
                print "Transferring"
                open_file = open(data[1],'wb')
                break
            else:
                print "File not found"
    else:
        print "Invalid Command"

