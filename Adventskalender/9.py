nums = list()
with open("data9.txt") as f:
    for num in f.readlines():
        nums.append(num)

s = sum(num[:24])
first=nums[0]
for i in range(25, len(nums)):
    if