n = int(input())
cp = sp = 100

for i in range(n) :
    c, s = map(int, input().split())

    if c < s :
        cp -= s
    elif c > s :
        sp -= c
    else :
        continue
        

print(cp, sp, sep='\n')