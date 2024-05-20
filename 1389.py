import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
graph = [[INF]*n for _ in range(n)]

for i in range(m):
    x, y = map(int, input().split())
    graph[x-1][y-1] = 1
    graph[y-1][x-1] = 1

for k in range(n):
    for i in range(n):
        for j in range(n):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
    
a, b = INF, 0
for i in range(n):
    graph[i][i] = 0
    tmp = sum(graph[i])
    if tmp < a:
        b = i
        a = tmp

print(b+1)