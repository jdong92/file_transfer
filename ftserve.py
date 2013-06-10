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
    match = 0
    data = conn.recv(4096)
    data = data.split()
    if not data: break
    elif data[0] == 'list' and len(data) == 1:
        files = [f for f in os.listdir('.') if os.path.isfile(f)]
        conn.send("/f"+str(files))
    elif data[0] == 'get' and len(data) == 2:
        files = [f for f in os.listdir('.') if os.path.isfile(f)]
        for f in files:
            if data[1] == f:
                open_file = open(data[1],'rb')
                send_file = open_file.read()
                open_file.close()
                #conn.send("SEND " + data[1])
                conn.send("/g"+data[1]+"/\n"+send_file)
                match = 1
        if match == 0:
            conn.send("/eFile Not Found\n")
    else:
        conn.send("/iInvalid Command\n")

