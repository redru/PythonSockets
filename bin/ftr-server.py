import os
import sys

# Add libs path to runtime and import libs
from libs.utils import JsonConf
from libs.utils import Fs
from libs.serversocket import Server

# Load configuration data
serverconf = JsonConf(cwd + '/conf/server_conf.json')
serverconf.load()

# Create download directory if not exists
Fs.createIfNotExists(serverconf.get("downloadDir"))

# Initialize socket server and start listening
server = Server(serverconf.get("address"), serverconf.get("port"), serverconf.get("downloadDir"))
server.start()
