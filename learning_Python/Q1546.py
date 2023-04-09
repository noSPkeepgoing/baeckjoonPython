N = int(input())
points = list(map(int, input().split()))
print(((sum(points) * 100 / max(points))) / N)