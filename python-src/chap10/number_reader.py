import json

filename = '/Users/baldoino/Workspace/software-project-course/python-src/chap10/numbers.json'
with open(filename) as f:
    numbers = json.load(f)
    
for number in numbers:
    print(number)