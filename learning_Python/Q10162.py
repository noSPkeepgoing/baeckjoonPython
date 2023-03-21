T = int(input())

A, B, C = 300, 60, 10

if T % 10 != 0 :
    print(-1)
else :
    TA = T // A
    TB = (T % A) // B
    TC = ((T % A) %  B) // C
    print(TA, TB, TC)
