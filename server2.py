# Echo server program
import socket
import thread

HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 4025              # Arbitrary non-privileged port

connections = []

def connectionsDataCallback(threadName, delay):
    for connection in connections:
        while 1:
            data = connection.recv(1024)
            if not data: break
            if data == 'close':
                connection.close()
                break

            connection.sendall(data)

soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
soc.bind((HOST, PORT))
soc.listen(10)

while 1:
    conn, addr = soc.accept()
    print 'Connected by', addr
    connections.append(conn)
    thread.start_new_thread(connectionsDataCallback, ("Thread-1", 50, ) )