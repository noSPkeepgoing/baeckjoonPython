import sys

prime = [True] * 1000001


for i in range(2, 1001):
    if prime[i]:
        for j in range(i * 2, 1000001, i):
            prime[j] = False


T = int(sys.stdin.readline())

for _ in range(T):
    count = 0
    N = int(sys.stdin.readline())
    n = N // 2 + 1
    for p in range(2, n):
        if prime[p] and prime[N-p]:
            count += 1
    print(count)
