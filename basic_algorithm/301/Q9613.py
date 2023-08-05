import sys

t = int(sys.stdin.readline())


def gcd(num1, num2):
    a, b = sorted([num1, num2], reverse=True)
    while True:
        r = a % b
        if r == 0:
            return b
        a, b = b, r


for _ in range(t):
    n, *nums = map(int, sys.stdin.readline().split())
    answer = 0
    for i, _ in enumerate(nums[:-1]):
        for num in nums[i+1:]:
            answer += gcd(nums[i], num)
    print(answer)
