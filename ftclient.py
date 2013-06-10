import socket

def transfer_file(data):
    fname = data.split()[0]
    fname = fname[2:-1]
    f = open(fname, "wb")
    f.write(data)
    f.close()
    print "File Transfer Complete!"

HOST = '127.0.0.1'
PORT = 9050

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error:
    print 'Failed to create socket'
    sys.exit()

s.connect((HOST, PORT))

while 1:
    filename = raw_input('list or get <filename>: \n')
    s.sendall(filename)
    data = s.recv(4096)
    if not data: break
    elif data[0:2] == "/g":
        #fname = data.split()[0]
        #fname = fname[2:-1]
        #f = open(fname,"wb")
        #f.write(data)
        #f.close()
        transfer_file(data)
    elif data[0:2] == "/f":
        print data[2:len(data)]
    elif data[0:2] == "/e":
        print "File Not Found! \n"
    elif data[0:2] == "/i":
        print "Invalid Command! \n"
