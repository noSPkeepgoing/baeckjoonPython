k = int(input())

for i in range(k):
    A, B = map(int,input().split())
    result = 'Case #{}: {}'.format(i+1, A+B)
    print(result)