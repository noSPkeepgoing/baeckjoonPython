num = 0
nums = []
for _ in range(4):
    outNum, inNum = map(int, input().split())
    addNum = inNum - outNum
    nums.append(num+addNum)
    num += addNum
print(max(nums))