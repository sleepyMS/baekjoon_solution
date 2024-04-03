import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = [int(input()) for _ in range(n)]
cnt, s = 0, 0

while s < k:
    coin = arr.pop()
    if s + coin <= k:
        tmp = (k-s) // coin
        s += coin * tmp
        cnt += tmp
        
print(cnt)


# 10 15              
n, k = map(int, input().split())
arr = []
coin = 0

for i in range(n):
    tmp = int(input())
    arr.append(tmp)

for i in range(1, n+1):
    if k >= arr[-i]:
        a = (k // arr[-i])
        coin = coin + a
        k = k - (arr[-i] * a)

print(coin)
