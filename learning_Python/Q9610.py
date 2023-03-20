n = int(input())

Q = [0 for i in range(5)]

for i in range(n) :
    x, y = map(int, input().split())

    if x * y == 0 :
        Q[4] += 1
    elif x * y > 0 :
        if x > 0 :
            Q[0] += 1
        else :
            Q[2] += 1
    else :
        if x > 0 :
            Q[3] += 1
        else :
            Q[1] += 1

for j in range(len(Q)) :
    if j == 4 :
        print('AXIS:', Q[j])
    else :
        print('Q{}: {}'.format(j + 1, Q[j]))