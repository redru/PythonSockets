import json
import os

class JsonConf:
    filepath = ""

    def __init__(self, filepath):
        if filepath:
            self.filepath = filepath

    def load(self):
        with open(self.filepath) as data_file:    
            self.__conf = json.load(data_file)
    
    def get(self, attr):
        return self.__conf[attr] if attr in self.__conf else ""

    def getList(self):
        attrlist = []
        for attr in self.__conf:
            attrlist.append(attr)

        return attrlist

    def add(self):
        try:
            key = raw_input("Name: ")
            address = raw_input("Address: ")
            port = int(raw_input("Port: "))

            if key not in self.__conf:
                self.__conf[key] = {"address": address, "port": port}

            open(self.filepath, 'wb').write(json.dumps(self.__conf))
            print "Correctly added a new friend: " + key + "@" + address + ":" + str(port)
        except ValueError:
            print "Port must be a number. Friend was not saved."

    def modify(self):
        return

    def remove(self):
        key = raw_input("REMOVE: ")
        if key in self.__conf:
            del self.__conf[key]
            open(self.filepath, 'wb').write(json.dumps(self.__conf))
        else:
            print "Key \"" + key + "\" was not found in friends list"


class Fs:
    @staticmethod
    def createIfNotExists(path):
        if not os.path.exists(path):
            os.makedirs(path)
            print "Created dir -> " + path

    @staticmethod
    def appendNumberIfExists(path, count=0):
        if os.path.isfile(path):
            if os.path.isfile(path + "_" + str(count)):
                return Fs.appendNumberIfExists(path, count + 1)
            else:
                return path + "_" + str(count)
        
        return path


class File():
    def __init__(self, path, mode):
        self.path = path
        self.stream = open(path, mode)
        self.size = os.path.getsize(path)

        splittedurl = str.split(path, "/")
        self.name = splittedurl[len(splittedurl) - 1]

