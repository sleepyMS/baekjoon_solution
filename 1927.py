import heapq
import sys
input = sys.stdin.readline


hq = []
for _ in range(int(input())):
    tmp = int(input())

    if tmp == 0:
        if not len(hq):
            print(0)
        else:
            print(heapq.heappop(hq))
    
    else:
        heapq.heappush(hq, tmp)