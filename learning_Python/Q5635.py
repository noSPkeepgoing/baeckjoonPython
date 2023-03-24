n = int(input())
names, births = [], []

for i in range(n) :
    name, *birth = input().split()
    birthday = (int(birth[-1]) * 10**4) + (int(birth[-2]) * 10**2) + (int(birth[-3]))

    names.append(name)
    births.append(birthday)
    
o_idx = births.index(min(births))
y_idx = births.index(max(births))

print(names[y_idx], names[o_idx], sep='\n')
