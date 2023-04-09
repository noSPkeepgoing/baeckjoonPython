N = int(input())
Q = list(map(int, input().split()))
point, total = 0, 0

for i in Q :
    if not i :
        point = 0
    else :
        point += 1
    total += point
print(total)