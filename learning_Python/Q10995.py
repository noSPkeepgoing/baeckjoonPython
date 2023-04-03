N = int(input())

for i in range(1, N + 1) :
    if(i % 2) :
        print(('* ' * N).rstrip())
    else :
        print(' *' * N)