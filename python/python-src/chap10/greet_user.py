import json

filename = '/Users/baldoino/Workspace/software-project-course/python-src/chap10/username.json'

with open(filename) as f:
    username = json.load(f)
    print(f"Welcome back, {username}!")