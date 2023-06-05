import sys
T = int(sys.stdin.readline())

for i in range(T):
    str = sys.stdin.readline().split()
    for s in str:
        print(s[::-1], end=' ')
    print()