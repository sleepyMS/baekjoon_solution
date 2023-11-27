import sys
from collections import deque
input = sys.stdin.readline

for _ in range(int(input())):
    x, y = map(int, input().split())
    que = list(map(int, input().split()))
    ind = list(i for i in range(len(que)))
    cnt = 0
    while y in ind:
        while max(que) != que[0]:
            que.append(que.pop(0))
            ind.append(ind.pop(0))
        que.pop(0)
        ind.pop(0)
        cnt += 1
    print(cnt)