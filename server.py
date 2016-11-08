import os
import socket
import sys
from sys import stdout
from datetime import datetime

from libs.parser import Parser

if len(sys.argv) > 1:
    sys.argv = Parser.parseCommandLineArguments(sys.argv[1:])
    print "Command line arguments -> " + str(sys.argv)

HOST = sys.argv["address"] if "address" in sys.argv else ""
PORT = int(sys.argv["port"]) if "port" in sys.argv else 50025
DOWNLOAD_DIR = sys.argv["downloadDir"] if "downloadDir" in sys.argv else "downloads"

if not os.path.exists(DOWNLOAD_DIR):
    os.makedirs(DOWNLOAD_DIR)
    print "Created download dir -> " + DOWNLOAD_DIR

print "Set download directory -> " + DOWNLOAD_DIR

def writeToFileConnectionData(connection, filename):
    file = open(filename, "ab")
    print "File opened:", filename

    received = 0
    while 1:
        data = connection.recv(4096000)
        if not data: break
        received += len(data)
        file.write(data)

        stdout.write("\rReceived[" + str(received) + " bytes]")
        stdout.flush()

    file.close()
    print "File closed:", filename

soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
soc.bind((HOST, PORT))
soc.listen(5)
print "Listening at " + HOST + ":" + str(PORT)

while 1:
    conn, addr = soc.accept()
    print "Connected by:", addr
    writeToFileConnectionData(conn, DOWNLOAD_DIR + "/" + datetime.now().strftime("%Y%m%d%H%M%S"))
    conn.close()
    print "Coonection closed:", addr