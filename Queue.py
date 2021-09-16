import math, sys
from collections import deque
queue = deque(range(10))

x = 1

queue.append(x) # добавление
x = queue.popleft() # удаление

# либо через двусвязный список на свой страх и риск

