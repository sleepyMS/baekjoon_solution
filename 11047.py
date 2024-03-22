import sys
input = sys.stdin.readline

n, k = map(int, input().split())
money = [int(input()) for _ in range(n)]
c, s = 0, 0

while s < k:
    if s + money[-1] <= k:
        tmp = (k-s) // money[-1]
        s += money[-1] * tmp
        c += tmp
        money.pop()
    else:
        money.pop()

print(c)