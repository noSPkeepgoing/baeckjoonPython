N = int(input())

for i in range(1, N + 1) :
    print(('*' * i).rjust(N))
for j in range(N - 1, 0, -1) :
    print(('*' * j).rjust(N))