filename = '/Users/baldoino/Workspace/software-project-course/python-src/chap10/pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())