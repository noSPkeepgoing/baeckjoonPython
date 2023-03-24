PH, PM, PS = map(int, input().split(':'))
SH, SM, SS = map(int, input().split(':'))

result = ((SH - PH) * 60**2) + ((SM - PM) * 60) + SS - PS 

if result < 0 :
    result += 24 * (60**2)
    
H = result // 60**2
M = (result % 60**2) // 60
S = (result % 60**2) % 60

print('{:02}:{:02}:{:02}'.format(H, M, S))