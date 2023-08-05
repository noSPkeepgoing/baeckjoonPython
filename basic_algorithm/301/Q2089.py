import sys

n = int(sys.stdin.readline())
res = []

while n:
    if n % -2:
        n = int(n // -2) + 1
        res.append(1)
    else:
        n = int(n // -2)
        res.append(0)

if res:
    res.reverse()
    print(*res, sep='')
else:
    print(0)
