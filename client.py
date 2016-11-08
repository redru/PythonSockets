# Client program
import socket
from sys import stdin
from sys import stdout

HOST = 'localhost'
PORT = 50025

soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
soc.connect((HOST, PORT))

print 'Connected to', HOST, ':', PORT
stdout.write('Send message: ')
stdout.flush()

soc.sendall(stdin.readline())
soc.close()