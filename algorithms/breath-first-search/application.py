from os import listdir
from os.path import isfile, join
from collections import deque

def printnames(start_dir):
    queue = deque()
    queue.append(start_dir)

    while queue:
        path = queue.popleft()
        for name in listdir(path):
            full_path = join(path, name)
            if isfile(full_path):
                print(name)
            else:
                queue.append(full_path)

printnames('../data')