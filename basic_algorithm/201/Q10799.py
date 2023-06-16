import sys

answer = 0
stack = []

stick = sys.stdin.readline().rstrip()

i = 0
while i < len(stick):
    if stick[i] == '(':
        if stick[i+1] == ')':
            answer += len(stack)
            i += 2
            continue
        else:
            stack.append(1)
    else:
        answer += stack.pop()
    i += 1

print(answer)
