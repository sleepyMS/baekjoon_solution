import sys
input = sys.stdin.readline

n = int(input())
nums = []
numdict = {}
for _ in range(n):
    num = int(input())
    nums.append(num)
    if num in numdict: 
        numdict[num] += 1
    else: 
        numdict[num] = 1

nums = sorted(nums)

print(round(sum(nums) / n))

print(nums[n//2])

maxcnt = max(numdict.values())
modes = list(filter(lambda x: numdict[x] == maxcnt, numdict.keys()))

if len(modes) == 1:
    print(modes[0])
else:
    print(sorted(modes)[1])

print(nums[-1] - nums[0])