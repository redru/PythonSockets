# Client program
import os
import socket
import sys
from sys import stdin
from sys import stdout

cwd = os.getcwd()
sys.path.append(cwd)

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
input_file_size = os.path.getsize(filepath)
input_file_name = str.split(filepath, "/")
input_file_name = input_file_name[len(input_file_name) - 1]
meta_data = str(input_file_size) + "|" + input_file_name + "|"

while len(meta_data) < 256:
    meta_data += "."

soc.send(meta_data)

readcount = 0

while 1:
    data = input_file.read(4096000)
    if not data: break
    readcount += len(data)
    stdout.write("\rRead[" + str(readcount) + " bytes]")
    stdout.flush()
    soc.send(data)

print "Sent file:", filepath
soc.close()