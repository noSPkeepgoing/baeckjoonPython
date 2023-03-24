M = int(input())
N = int(input())
nums = []

for i in range(M, N + 1) :
    if i**(1/2) % 1 == 0 :
        nums.append(i)

if len(nums) == 0 :
    print(-1)
else :
    print(sum(nums), nums[0], sep='\n')

