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

#if data.get(0) == 'list' and data.length == 1
#if data.get(0) == 'get' and data.length == 2

while 1:
    data = conn.recv(1024)
    if not data: break
    elif data == 'list':
        files = [f for f in os.listdir('.') if os.path.isfile(f)]
        for f in files:
            print f
    elif data == 'get'
        print 'Invalid Command'

conn.close()
