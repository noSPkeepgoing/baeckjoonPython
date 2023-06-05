import sys

stackList = []

def stack(op):
    oper = op.split()
    
    if oper[0] == 'push' :
        stackList.append(int(oper[1]))
    elif oper[0] == 'pop':
        pop = stackList.pop() if len(stackList) else -1
        print(pop)
    elif oper[0] == 'size':
        print(len(stackList))
    elif oper[0] == 'empty':
        empty = 0 if len(stackList) else 1
        print(empty)
    else :
        top = stackList[-1] if len(stackList) else -1
        print(top)

N = int(sys.stdin.readline())
for i in range(N):
    stack(sys.stdin.readline())