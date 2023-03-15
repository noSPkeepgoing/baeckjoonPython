N = int(input())

vote = []
for i in range(N) :
    vote.append(int(input()))

print('Junhee is not cute!' if vote.count(0) > vote.count(1) else 'Junhee is cute!')
