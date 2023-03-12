T = int(input())

for i in range(T) :
    B, A = sorted(map(int, input().split()))
    M = A * B
    while True :
        R = A % B
        if R == 0 :
            print(M // B)
            break;
        A = B
        B = R
    