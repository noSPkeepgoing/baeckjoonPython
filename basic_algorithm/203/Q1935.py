import sys

n = int(sys.stdin.readline())
postfix = list(sys.stdin.readline().rstrip())
stack = []

for i in range(n):
    s = input()
    for j in postfix:
        if j == chr(65+i):
            postfix[postfix.index(j)] = s

for p in postfix:
    if p.isdigit():
        stack.append(p)
    else:
        post = stack.pop()
        pre = stack.pop()
        stack.append(str(eval(pre + p + post)))

print('{:.2f}'.format(float(stack.pop())))
