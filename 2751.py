import sys
input = sys.stdin.readline

testCase = int(input())
sortList = [int(input().rstrip()) for _ in range(testCase)]

sortList = sorted(sortList)

for s in sortList:
    print(s)