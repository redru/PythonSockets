import os
import sys

# Add libs path to runtime and import libs
cwd = os.getcwd()
sys.path.append(cwd)
from libs.parser import Parser
from libs.utils import JsonConf
from libs.utils import Fs
from libs.serversocket import Server

# Load configuration data
serverconf = JsonConf(cwd + '/conf/server_conf.json')

# Create download directory if not exists
Fs.createIfNotExists(serverconf.get("downloadDir"))

# Initialize socket server and start listening
server = Server(serverconf.get("address"), serverconf.get("port"), serverconf.get("downloadDir"))
server.start()