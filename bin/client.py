# Client program
import os
import socket
import sys
from sys import stdout

CWD = os.getcwd()
sys.path.append(CWD)
from libs.utils import JsonConf
from libs.parser import Parser

# Load configuration data
if len(sys.argv) == 3:
    print "Loading " + CWD + "/conf/friends.json" + " configuration"
    friends = JsonConf(CWD + "/conf/friends.json")
    conn_data = friends.get(sys.argv[2])

if len(sys.argv) == 4:
    print "Loading friends.json configuration"
    params = Parser.parseCommandLineArguments(sys.argv[1:])
    conn_data = {"address": params["address"], "port": params["port"]}

# Set file path to transfer
filepath = sys.argv[1]

soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
soc.connect((conn_data["address"], int(conn_data["port"])))
print "Connected to " + conn_data["address"] + ':' + str(conn_data["port"])

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