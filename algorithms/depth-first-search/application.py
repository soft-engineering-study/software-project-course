from os import listdir
from os.path import isfile, join

def printnames(dir):
    for name in sorted(listdir(dir)):
        fullpath = join(dir, name)
        if isfile(fullpath):
            print(fullpath)
        else:
            printnames(fullpath)

printnames('../data')