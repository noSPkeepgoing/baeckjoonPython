T = int(input())

for i in range(1, T + 1) :
    print('Case {}: {}'.format(i, sum(map(int, input().split()))))