x = int(input())
y = int(input())
xy = x * y

while( y != 0):
    n = y % 10
    print(x * n)
    y = y // 10

print(xy)