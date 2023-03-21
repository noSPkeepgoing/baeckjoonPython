T = int(input())

for i in range(T) :
    yp = kp = 0

    for j in range(9) :
        y, k = map(int,input().split())
        yp += y
        kp += k
    
    if yp > kp :
        print('Yonsei')
    elif yp < kp :
        print('Korea')
    else :
        print('Draw')


