N = int(input())
result = []
for i in range(N) :
    dice = list(map(int, input().split()))
    dice.sort()

    if dice.count(dice[1]) == 1 :
        money = dice[2] * 100
    elif dice.count(dice[1]) == 2 :
        money = 1000 + dice[1] * 100
    else :
        money = 10000 + dice[1] * 1000
   
    result.append(money)

print(max(result))