from collections import deque

d = deque("hello", maxlen=5)
print(d)
d.append(1)
print(d)