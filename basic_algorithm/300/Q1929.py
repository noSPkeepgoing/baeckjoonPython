import sys

M, N = map(int, sys.stdin.readline().split())

for num in range(M, N+1):
    for n in range(2, int(num**0.5) + 1):
        if num % n == 0:
            break
    else:
        if num != 1:
            print(num)
