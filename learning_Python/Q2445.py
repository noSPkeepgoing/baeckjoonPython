N = int(input())

for i in range(1, N) :
    print(('*' * i).ljust(N), ('*' * i).rjust(N), sep='')
for j in range(N, 0, -1) :
    print(('*' * j).ljust(N), ('*' * j).rjust(N), sep='')
