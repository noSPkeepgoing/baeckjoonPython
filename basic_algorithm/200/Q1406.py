import sys

rightStack = []
leftStack = list(sys.stdin.readline().strip())
n = int(sys.stdin.readline())
for _ in range(n):
    oper = sys.stdin.readline().split()
    if oper[0] == 'L':
        if len(leftStack) == 0:
            continue
        rightStack.append(leftStack.pop())
    if oper[0] == 'D':
        if len(rightStack) == 0:
            continue
        leftStack.append(rightStack.pop())
    if oper[0] == 'B':
        if len(leftStack) == 0:
            continue
        leftStack.pop()
    if oper[0] == 'P':
        leftStack.append(oper[1])


print(''.join(leftStack + rightStack[-1::-1]))
