T = int(input())

for i in range(T) :
    point = 0
    sum = 0
    result = input()

    for j in range(len(result)) :
        if result[j] == 'O' :
            sum += 1
            point += sum
        else :
            sum = 0    

    print(point)