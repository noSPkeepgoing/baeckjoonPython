import sys

T = int(sys.stdin.readline())

for _ in range(T):
    str = sys.stdin.readline().strip()
    stack = []
    for s in str :
        if s == '(' :
            stack.append(s)
        else :
            if stack :
                stack.pop()
            else :
                print("NO")
                break;
    else :        
        if not stack :
            print("YES")
        else :
            print("NO")
