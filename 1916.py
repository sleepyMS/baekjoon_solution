import heapq
import sys
INF = sys.maxsize
input = sys.stdin.readline


n = int(input())
m = int(input())
bus = [[] for _ in range(n)]
for _ in range(m):
    a, b, c = map(int, input().split())
    bus[a-1].append((b-1, c))
    
a, b = map(int, input().split())

que = []
heapq.heappush(que, (0, a-1))
check = [INF for _ in range(n)]
check[a-1] = 0
while que:
    count, city = heapq.heappop(que)   
    if city == b-1:
        break
    for c, cnt in bus[city]:
        if count+cnt < check[c]:
            check[c] = count+cnt
            heapq.heappush(que, (count+cnt, c))
            
print(check[b-1])