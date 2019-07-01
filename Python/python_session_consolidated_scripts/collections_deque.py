from collections import deque

d = deque()
d.insert(0,2)
d.insert(0,3)
d.insert(0,5)
print(d)
d.pop()
print(d)
d.popleft()
print(d)
d.insert(1,77)
d.insert(2,33)
print(d)
