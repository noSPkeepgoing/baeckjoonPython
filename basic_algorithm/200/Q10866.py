import sys
from collections import deque

N = int(sys.stdin.readline())
deque = deque()

for _ in range(N):
    oper = sys.stdin.readline().split()
    
    if oper[0] == 'push_front':
        deque.append(oper[1])
    elif oper[0] == 'push_back' :
        deque.appendleft(oper[1])
    elif oper[0] == 'pop_front' :
        item = deque.pop() if deque else -1
        print(item)
    elif oper[0] == 'pop_back' :
        item = deque.popleft() if deque else -1
        print(item)
    elif oper[0] == 'size' :
        print(len(deque))
    elif oper[0] == 'empty' :
        size = 0 if deque else 1
        print(size)
    elif oper[0] == 'front' :
        item = deque[-1] if deque else -1
        print(item)
    elif oper[0] == 'back' :
        item = deque[0] if deque else -1
        print(item)