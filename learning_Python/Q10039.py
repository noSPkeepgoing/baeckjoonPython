import sys

points = [sys.stdin.readline().strip() for i in range(5)]

sum = 0
for p in points :
    if int(p) >= 40 :
        sum = sum + int(p)
    else :
        sum = sum + 40

print(int(sum/5))