import os
import sys
from sys import stdout

CWD = os.getcwd()
sys.path.append(CWD)
from libs.utils import JsonConf

friends = JsonConf(CWD + "/conf/friends.json")
friends.load()
print "Loaded " + CWD + "/conf/friends.json"

while 1:
    option = input("[1] List - [2] Add - [3] Modify - [4] Remove - [0] Exit\nSelect one: ")

    if option == 1:
        print friends.getList()

    elif option == 2:
        friends.add()

    elif option == 3:
        friends.modify()

    elif option == 4:
        friends.remove()

    elif option == 0:
        break

    else:
        print "Wrong option\n"
