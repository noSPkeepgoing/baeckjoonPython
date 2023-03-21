T = int(input())

for i in range(T) :
    N = int(input())
    S, L = [], []
    for j in range(N):
        s, l = input().split()
        S.append(s) 
        L.append(int(l))
    index = L.index(max(L))
    print(S[index])
