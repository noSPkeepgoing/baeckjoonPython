N = int(input())

for i in range(1, N + 1) :
    print(('*' * (2 * i - 1)).center(2 * N - 1).rstrip())