import sys
input = sys.stdin.readline

sortList = list()
for _ in range(int(input())):
    x, y = map(int, input().split())

    sortList.append([x, y])

sortList = sorted(sortList, key=lambda x:(x[0], x[1]))
for s in sortList:
    print(s[0], s[1])