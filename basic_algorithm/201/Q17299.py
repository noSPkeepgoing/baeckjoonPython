import sys
from collections import Counter

N = int(sys.stdin.readline())
A = [i for i in map(int, sys.stdin.readline().split())]
counter = Counter(A)
answer = [-1] * N
stack = []


for i in range(N):
    while stack and counter[A[stack[-1]]] < counter[A[i]]:
        answer[stack.pop()] = A[i]
    stack.append(i)

print(*answer)
