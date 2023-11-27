import sys
input = sys.stdin.readline

sortList = list()
for _ in range(int(input())):
    x, y = map(int, input().split())

    sortList.append([x, y])

sortList = sorted(sortList, key=lambda x:(x[1], x[0]))
for s in sortList:
    print(s[0], s[1])