import socket
from sys import stdout

class ClientSocket:

    def __init__(self, address, port):
        self.address = address
        self.port = port
    
    def connect(self):
        self.soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.soc.connect((self.address, self.port))
        print ("Connected to " + self.address + ':' + str(self.port))

    def write(self, data):
        self.soc.send(data)

    def writeFile(self, file, chunkssize):
        readcount = 0

        while 1:
            data = file.stream.read(chunkssize)
            if not data: break
            readcount += len(data)
            stdout.write("\rRead[" + str(readcount) + " bytes]")
            stdout.flush()
            self.write(data)

        print ("")

    def writeMetadata(self, metadata):
        while len(metadata) < 256:
            metadata += "."

        self.soc.send(bytearray(metadata, "utf8"))

    def close(self):
        self.soc.close()
