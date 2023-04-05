N = int(input())
numbers = list(map(int, input().split()))
count = 0

for i in numbers :
    for j in range(2, i + 1) :
        if j == i :
            count += 1
        elif i % j == 0 :
            break
print(count)

