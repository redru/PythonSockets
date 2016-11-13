# Client program
import os
import sys

from libs.utils import JsonConf
from libs.utils import File
from libs.parser import Parser
from libs.clientsocket import ClientSocket


CWD = os.getcwd()

# Load configuration data
if len(sys.argv) == 3:
    print ("Loading " + CWD + "/conf/friends.json" + " configuration")
    friends = JsonConf(CWD + "/conf/friends.json")
    friends.load()
    conn_data = friends.get(sys.argv[2])

if len(sys.argv) == 4:
    print ("Loading friends.json configuration")
    params = Parser.parseCommandLineArguments(sys.argv[1:])
    conn_data = {"address": params["address"], "port": params["port"]}

conn = ClientSocket(conn_data["address"], int(conn_data["port"]))
conn.connect()

inputfile = File(sys.argv[1], 'rb')
conn.writeMetadata(str(inputfile.size) + "|" + inputfile.name + "|")
conn.writeFile(inputfile, 4096000)

print ("Sent file: " + inputfile.path)
conn.close()
