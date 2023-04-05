N, K = map(int, input().split())
prime = []

for i in range(1, N + 1) :
    if not (N % i) :
        prime.append(i)

result = prime[K - 1] if len(prime) >= K else 0
print(result)