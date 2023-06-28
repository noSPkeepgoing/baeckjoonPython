import sys

n, m = map(int, sys.stdin.readline().split())


def count(num, k):
    cnt = 0
    while num:
        cnt += num//k
        num //= k
    return cnt


countnumber2 = count(n, 2)-count(m, 2)-count(n-m, 2)
countnumber5 = count(n, 5)-count(m, 5)-count(n-m, 5)

print(min(countnumber2, countnumber5))
