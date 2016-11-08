import socket
import sys
from datetime import datetime
from sys import stdout
from utils import Fs

class Server:
    
    def __init__(self, address, port, downloaddir):
        self.address = address
        self.port = port
        self.downloaddir = downloaddir
        self.serversoc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.serversoc.bind((self.address, self.port))
        self.serversoc.listen(5)
        print "Set download directory -> " + self.downloaddir
        print "Waiting for connections at " + self.address + ":" + str(self.port)

    def start(self):
        while 1:
            self.conn, addr = self.serversoc.accept()
            print "Connected by:", addr
            self.readFromConnectionToFile()
            self.conn.close()
            print "Coonection closed:", addr

    def write(self):
        return

    def readFromConnectionToFile(self):
        # Retrieve metadata
        data = self.conn.recv(256)
        data = str.split(data, "|")

        # Set file directory and file name
        filedir = self.downloaddir + "/" + data[1]
        filedir = Fs.appendNumberIfExists(filedir)

        # Open file
        file = open(filedir, "ab")
        print "File opened:", filedir

        received = 0
        while 1:
            # Read chunk
            data = self.conn.recv(4096000)
            # Break if any data was received
            if not data: break
            # Update counter and write chunk to file
            received += len(data)
            file.write(data)

            # Update console status
            stdout.write("\rReceived[" + str(received) + " bytes]")
            stdout.flush()

        # When finished reading and writing, close file
        file.close()
        print "\nFile closed:", filedir


class ServerSocket:

    def __init__(self):
        return