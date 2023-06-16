import sys

S = sys.stdin.readline().rstrip() + ' '
result = ''
stack = []
istag = False

for s in S:
    if s == '<':
        istag = True
    elif s == '>':
        istag = False
        result += s
        continue

    if istag:
        while stack:
            result += stack.pop()
        result += s
    else:
        if s == ' ':
            while stack:
                result += stack.pop()
            result += ' '
        else:
            stack.append(s)

print(result)
