import sys
input = sys.stdin.readline

k, n = map(int, input().split())
lan = []

for _ in range(k):
    lan.append(int(input()))

maxLen = sum(lan) // n
minLen = 1

while minLen <= maxLen:
    midLen = (minLen + maxLen) // 2
    result = 0
    for i in lan:
        result += i // midLen
    
    if result >= n:
        minLen = midLen + 1
    elif result < n:
        maxLen = midLen - 1

print(minLen - 1)