import sys

queueList = []

def queue(op):
    oper = op.split()
    
    if oper[0] == 'push' :
        queueList.append(int(oper[1]))
    elif oper[0] == 'pop':
        pop = queueList.pop(0) if len(queueList) else -1
        print(pop)
    elif oper[0] == 'size':
        print(len(queueList))
    elif oper[0] == 'empty':
        empty = 0 if len(queueList) else 1
        print(empty)
    elif oper[0] == 'front':
        front = queueList[0] if len(queueList) else -1
        print(front)
    else :
        back = queueList[-1] if len(queueList) else -1
        print(back)


N = int(sys.stdin.readline())
for i in range(N):
    queue(sys.stdin.readline())