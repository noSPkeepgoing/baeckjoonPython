import sys

prime = [True] * 1000001

for i in range(2, 1001):
    if prime[i]:
        for j in range(i * 2, 1000001, i):
            prime[j] = False


while True:
    n = int(sys.stdin.readline())
    if n == 0:
        break
    for i in range(3, n, 2):
        if prime[i] and prime[n - i]:
            print('{} = {} + {}'.format(n, i, n-i))
            break
    else:
        print("Goldbach's conjecture is wrong.")
