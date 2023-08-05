import sys


def gcd(num1, num2):
    b, a = sorted([num1, num2])
    while True:
        r = a % b
        if r == 0:
            return b
        a, b = b, r


N, S = map(int, sys.stdin.readline().split())
A = [abs(S - n) for n in map(int, sys.stdin.readline().split())]

while len(A) > 1:
    num = gcd(A.pop(), A.pop())
    A.append(num)

print(*A)
