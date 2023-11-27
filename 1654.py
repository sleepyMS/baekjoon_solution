import sys
input = sys.stdin.readline

k, n = map(int, input().split())
length = [int(input()) for _ in range(k)]
base = min(length)
div, count = 0, 0

while count <= n:
    div += 1
    tmp = base // div
    count = 0
    for i in length:
        count += i // tmp

base1, base2 = None, None
if div == 1:
    dase1, base2 = base, base
else:
    base1, base2 = base // div, base // (div-1)


for i in range(base2, base1-1, -1):
    count = 0
    for j in length:
        count += j // i
    if count >= n:
        print(i)
        break

