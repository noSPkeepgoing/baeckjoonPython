T = int(input())

for _ in range(T) :
    price = int(input())
    n = int(input())
    for _ in range(n) :
        q, p = map(int, input().split())
        price += q * p
    print(price)
