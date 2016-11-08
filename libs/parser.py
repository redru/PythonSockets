# Parser class for many things
class Parser:

    # Function that parses command line arguments and returns a dictionary
    @staticmethod
    def parseCommandLineArguments(args):
        result = {}
        for arg in args:
            tmp = str.split(arg, "=")
            result[tmp[0]] = (tmp[1] if len(tmp) == 2 else "")
        
        return result