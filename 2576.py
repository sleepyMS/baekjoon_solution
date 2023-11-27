import sys
input = sys.stdin.readline

oddList = list()
for _ in range(7):
    tmp = int(input())
    if tmp % 2 == 1:
        oddList.append(tmp)

if not oddList:
    print(-1)
else:
    print(sum(oddList))
    print(min(oddList))