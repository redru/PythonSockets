import os
import sys
from sys import stdout

CWD = os.getcwd()
sys.path.append(CWD)
from libs.utils import JsonConf

print """####################################
# Welcome to FTR command line conf #
####################################"""
friends = JsonConf(CWD + "/conf/friends.json")
friends.load()

while 1:
    option = raw_input(">>>>>>>>>>\n[1] List - [2] Add - [3] Modify - [4] Remove - [0] Exit\nSelect one: ")

    if option == "1":
        print friends.getList()

    elif option == "2":
        friends.add()

    elif option == "3":
        friends.modify()

    elif option == "4":
        friends.remove()

    elif option == "0":
        break

    else:
        print "Wrong option"
