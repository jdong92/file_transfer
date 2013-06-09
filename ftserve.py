import socket
import os

HOST = '127.0.0.1'
PORT = 9050

try:
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
except socket.error:
    print 'Failed to create socket'
    sys.exit()

sock.bind((HOST, PORT))
sock.listen(10)

conn, addr = sock.accept()

print 'Connect by', addr

while 1:
    data = conn.recv(4096)
    data = data.split()
    if not data: break
    elif data[0] == 'list' and len(data) == 1:
        files = [f for f in os.listdir('.') if os.path.isfile(f)]
        conn.send('List'+str(files))
    elif data[0] == 'get' and len(data) == 2:
        files = [f for f in os.listdir('.') if os.path.isfile(f)]
        for f in files:
            if data[1] == f:
                open_file = open(data[1],'rb')
                send_file = open_file.read()
                open_file.close()
                conn.send(send_file)
                break
            else:
                conn.send("File not found\n")
    else:
        conn.send("Invalid Command\n")

