H, M = map(int, input().split())

if M >= 45 :
    print(H, M - 45)
else :
    print(23 if H < 1 else H - 1, M + 15)