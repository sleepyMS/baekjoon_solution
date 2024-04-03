import heapq
import sys
input = sys.stdin.readline


n = int(input())
hq_min = []
hq_max = []
for i in map(int, input().split()):
    heapq.heappush(hq_min, i)
    heapq.heappush(hq_max, (-i, i))

print(heapq.heappop(hq_min), heapq.heappop(hq_max)[1])

