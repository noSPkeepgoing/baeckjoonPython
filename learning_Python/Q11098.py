n = int(input())

for i in range(n) :
    p = int(input())
    c = 0 
    for j in range(p) :
        C, name = input().split()
        if int(C) > c :
            result = name
            c = int(C)
    print(result)
        