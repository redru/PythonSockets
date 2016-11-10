import json
import os

class JsonConf:
    __conf = None

    def __init__(self, filepath):
        if filepath:
            self.load(filepath)

    def load(self, filepath):
        with open(filepath) as data_file:    
            self.__conf = json.load(data_file)
    
    def get(self, attr):
        return self.__conf[attr] if attr in self.__conf else ""


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
