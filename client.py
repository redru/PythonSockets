# Client program
import socket
from sys import stdin
from sys import stdout

HOST = 'localhost'
PORT = 4025

soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
soc.connect((HOST, PORT))

print 'Connected to', HOST, ':', PORT
stdout.write('Send message: ')
stdout.flush()

soc.sendall(stdin.readline())

data = soc.recv(1024)
if data:
    stdout.write('Message received: ' + data)

soc.close()