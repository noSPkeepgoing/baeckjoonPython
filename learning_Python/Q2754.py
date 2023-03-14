grade = input()
point = 0

for i in grade :
    if i == 'A' :
        point += 4
    elif i == 'B' :
        point += 3
    elif i == 'C' :
        point += 2
    elif i == 'D' :
        point += 1
    elif i == 'F' :
        break

    if i == '+' :
        point += 0.3
    elif i == '-' :
        point -= 0.3

print(float(point))
