N = int(input())
sum = 0

for _ in range(N) :
    s, a = map(int, input().split())
    sum += a % s
print(sum)