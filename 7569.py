from queue import deque
import sys
input = sys.stdin.readline


def BFS(graph):
    global m, n, h
    before = []
    after = {(i, j, k): 0 if graph[i][j][k] else before.append((i, j, k)) for i in range(h) for j in range(n) for k in range(m)}
    if not before:
        return 0
    
    que = deque([t for t, i in after.items() if graph[t[0]][t[1]][t[2]] == 1])
    
    while que:
        x, y, z = que.popleft()
        
        for i, j, k in [(-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1)]:
            nx, ny, nz = x + i, y + j, z + k
            if 0 <= nx < h and 0 <= ny < n and 0 <= nz < m and not graph[nx][ny][nz]:
                after[(nx, ny, nz)] = after[(x, y, z)] + 1
                graph[nx][ny][nz] = after[(x, y, z)] + 1
                que.append((nx, ny, nz))
    
    tmp = [graph[i][j][k] for i, j, k in before]
    result = -1 if not min(tmp) else max(tmp)
    
    return result
    

if __name__ == "__main__":
    m, n, h = map(int, input().split())
    graph = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]
    print(BFS(graph))