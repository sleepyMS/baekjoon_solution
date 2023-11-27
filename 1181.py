import sys
input = sys.stdin.readline

testCase = int(input())
sortList = list(set([input().rstrip() for _ in range(testCase)]))

sortList = sorted(sorted(sortList), key=lambda x: len(x))

for s in sortList:
    print(s)