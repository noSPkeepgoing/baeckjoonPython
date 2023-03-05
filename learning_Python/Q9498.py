P = int(input())
D = ''

if P >= 90 :
    D = 'A'
elif P >= 80 :
    D = 'B'
elif P >= 70 :
    D = 'C'
elif P >= 60 :
    D = 'D'
else :
    D = 'F'

print(D)