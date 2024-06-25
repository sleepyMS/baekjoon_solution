import heapq
import sys
input = sys.stdin.readline
INF = 1e+9


def dijkstra(graph, start):
    distance = {i: INF if i != start else 0 for i in graph}
    que = [(0, start)]

    while que:
        dis, cur = heapq.heappop(que)

        if dis > distance[cur]:
            continue
        for node, node_len in graph[cur].items():
            tmp = distance[cur] + node_len
            if tmp < distance[node]:
                distance[node] = tmp
                heapq.heappush(que, (tmp, node))

    return distance.values()


v, e = map(int, input().split())
k = int(input())

graph = {i: {} for i in range(1, v+1)}
for u, v, w in [map(int, input().split()) for _ in range(e)]:
    graph[u][v] = min(graph[u][v], w) if v in graph[u] else w

for i in dijkstra(graph, k):
    print(i if i < INF else "INF")
