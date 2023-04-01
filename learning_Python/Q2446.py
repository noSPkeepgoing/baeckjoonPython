N = int(input())

for i in range(N, 0, -1) :
    print(('*' * (2 * i - 1)).center(2 * N - 1).rstrip())
for j in range(2, N + 1) :
    print(('*' * (2 * j - 1)).center(2 * N - 1).rstrip())
    