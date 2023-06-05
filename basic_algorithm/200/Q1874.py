import sys

n = int(sys.stdin.readline())
sequence = []
for _ in range(n):
    sequence.append(int(sys.stdin.readline()))

stack = []
start = 1
answer = []
for num in sequence:
    for _ in range(start, num + 1):
        answer.append('+')
        stack.append(_)
        start += 1 
    peek = stack[-1]
    if peek == num :
        answer.append('-')
        stack.pop()
    else :
        answer.append('ERROR')
        break
    
if 'ERROR' in answer:
    print("NO")
else :
    for _ in answer:
        print(_)


