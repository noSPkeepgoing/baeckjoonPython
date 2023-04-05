M = int(input())
N = int(input())
prime = []

for i in range(M, N + 1) :
    for j in range(2, i + 1) :
        if j == i :
            prime.append(i)
        elif i % j == 0 :
            break

if len(prime) == 0 :
    print(-1)
else : 
    print(sum(prime), prime[0], sep='\n')