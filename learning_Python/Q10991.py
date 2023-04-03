N = int(input())

for i in range(1, N + 1) :
    print(('* ' * i).rstrip().center(2 * N - 1).rstrip())

# n = int(input())

# for i in range(1, n+1):
#      print(' ' * (n-i) + '* ' * i)