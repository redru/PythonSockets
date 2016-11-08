# Echo server program
import os
import socket
import sys
from sys import stdout
from datetime import datetime

HOST = ""                 # Symbolic name meaning all available interfaces
PORT = 50025              # Arbitrary non-privileged port
DOWNLOAD_DIR = "downloads"

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

def createDownloadDir(path):
    if not os.path.exists(path):
        os.makedirs(path)

createDownloadDir(DOWNLOAD_DIR)

soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
soc.bind((HOST, PORT))
soc.listen(5)

while 1:
    conn, addr = soc.accept()
    print "Connected by:", addr
    writeToFileConnectionData(conn, DOWNLOAD_DIR + "/" + datetime.now().strftime("%Y%m%d%H%M%S"))
    conn.close()
    print "Coonection closed:", addr