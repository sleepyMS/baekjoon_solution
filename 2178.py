import sys
from collections import deque
input = sys.stdin.readline

def bfs(a, b):
    global graph, road
    que = deque()
    que.append((a, b))
    while que:
        current = que.popleft()
        
        for x, y in road:
            if 0 <= current[0] + x < n and 0 <= current[1] + y < m and graph[current[0] + x][current[1] + y] == 1:
                graph[current[0] + x][current[1] + y] = graph[current[0]][current[1]] + 1
                nx = current[0] + x
                ny = current[1] + y
                que.append((nx, ny))

    return graph[n-1][m-1]

n, m = map(int, input().split())
graph = [list(map(int, input().rstrip())) for _ in range(n)]
road = [(-1,0),(1,0),(0,-1),(0,1)]
print(bfs(0, 0))