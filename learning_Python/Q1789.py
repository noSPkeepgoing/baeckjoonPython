S = int(input())

for i in range(S + 1):
    S = S - i
    if S <= i :
        print(i)
        break