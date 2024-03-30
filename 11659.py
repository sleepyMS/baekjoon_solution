import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nArr = list(map(int, input().split()))

sumArr, s = [0], 0
for i in nArr:
    s += i
    sumArr.append(s)
    
for _ in range(m):
    start, end = map(int, input().split())
    print(sumArr[end] - sumArr[start-1])