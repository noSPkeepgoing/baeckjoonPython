import sys

infix = sys.stdin.readline().rstrip()
stack = []
postfix = ''

for s in infix:
    if s.isalpha():
        postfix += s
    else:
        if s == '(':
            stack.append(s)
        elif s == ')':
            while stack[-1] != '(':
                postfix += stack.pop()
            stack.pop()
        else:
            while stack:
                if stack[-1] == '(' or stack[-1] in '+-' and s in '*/':
                    break
                postfix += stack.pop()
            stack.append(s)
while stack:
    postfix += stack.pop()

print(postfix)
