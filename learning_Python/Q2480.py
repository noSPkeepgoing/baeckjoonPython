dice = list(map(int, input().split()))
dice.sort()

if dice.count(dice[1]) == 1 :
    result = dice[2] * 100
elif dice.count(dice[1]) == 2 :
    result = 1000 + dice[1] * 100
else :
    result = 10000 + dice[1] * 1000

print(result)
