# Client program
import socket
import sys
from sys import stdin
from sys import stdout

if len(sys.argv) < 4:
    print "[ERROR] Missing parameters. Expected 3 but got", (len(sys.argv) - 1)
    sys.exit(1)

HOST = sys.argv[1]
PORT = int(sys.argv[2])

soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
soc.connect((HOST, PORT))
print 'Connected to', HOST, ':', PORT

filepath = sys.argv[3]
input_file = open(filepath, 'rb')

readcount = 0

while 1:
    data = input_file.read(4096000)
    if not data: break
    readcount += len(data)
    stdout.write("\rRead[" + str(readcount) + " bytes]")
    stdout.flush()
    soc.send(data)
    # soc.recv(4096)

print "Sent file:", filepath
soc.close()