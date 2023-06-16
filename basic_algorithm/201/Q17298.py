import sys

N = int(sys.stdin.readline())
A = [i for i in map(int, sys.stdin.readline().split())]
answer = [-1] * N
stack = []

for i in range(N):
    while stack and A[stack[-1]] < A[i]:
        answer[stack.pop()] = A[i]
    stack.append(i)

print(*answer)
