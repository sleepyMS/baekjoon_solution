import heapq
import sys
input = sys.stdin.readline

n = int(input())
hq = []
for _ in range(n):
    tmp = int(input())
    if tmp:
        heapq.heappush(hq, (-tmp, tmp))
    elif hq:
        print(heapq.heappop(hq)[1])
    else:
        print(0)
