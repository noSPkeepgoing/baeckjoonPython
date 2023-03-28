nums =[0, 1]
n = int(input())

for i in range(2, n + 1) :
    nums.append(sum(nums[-1:-3:-1]))

print(nums[n])
