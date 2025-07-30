import json

numbers = [2, 4, 5, 7, 11, 13]

filename = '/Users/baldoino/Workspace/software-project-course/python-src/chap10/numbers.json'
with open(filename, 'w') as f:
    json.dump(numbers, f)