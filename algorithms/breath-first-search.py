from collections import deque
from dataset import graph

def person_is_seller(name):
    return name[-1]=='m'
def searchBreathFirst(name):
    queue = deque()
    queue += graph[name]
    searched = set()
    while queue:
        person = queue.popleft()
        print(person)
        for person in graph[person]:
            if person not in searched:
                if person_is_seller(person):
                    print(person + " is a mango seller")
                    return True
                else:
                    queue += graph[person]
                    searched.add(person)


searchBreathFirst("you")

