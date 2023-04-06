nums = []
odd = []
exec('nums.append(int(input()));' * 7) 

for i in nums :
    if i % 2 :
        odd.append(i)

if len(odd) :
    print(sum(odd), min(odd), sep='\n')
else :
    print(-1)