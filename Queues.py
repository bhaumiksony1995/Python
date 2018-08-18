# It is also possible to use a list as a queue, where the first element added is the first element retrieved (“first-in, first-out”); however, lists are not efficient for this purpose. While appends and pops from the end of list are fast, doing inserts or pops from the beginning of a list is slow (because all of the other elements have to be shifted by one).

#To implement a queue, use collections.deque which was designed to have fast appends and pops from both ends.

from collections import deque

queue = deque(["Eric", "John", "Michael"])
print(queue)
queue.append("Terry") # Terry arrives
queue.append("Graham") #Graham arrives
print(queue)
queue.popleft() # the first to arrive now leaves
queue.popleft() # second to arrive now leaves
print(queue)
