# Echo server program
import socket

HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 4025              # Arbitrary non-privileged port

soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
soc.bind((HOST, PORT))
soc.listen(1)

conn, addr = soc.accept()
print 'Connected by', addr

while 1:
    data = conn.recv(1024)
    if not data: break
    conn.sendall(data)

conn.close()