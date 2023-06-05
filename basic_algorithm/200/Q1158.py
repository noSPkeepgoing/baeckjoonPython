import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())
nums = deque(range(1, N+1))
order = []

while nums:
    for _ in range(K - 1):
        nums.append(nums.popleft())
    order.append(nums.popleft())

print('<'+', '.join(map(str, order))+'>')
