import sys

N = int(sys.stdin.readline())
mult = [int(sys.stdin.readline()) for _ in range(N)] 
print(sum(mult) - (N - 1))