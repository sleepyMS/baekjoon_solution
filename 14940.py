from queue import deque
import sys
input = sys.stdin.readline


def BFS(filed, n, m):
    que = deque([])
    result = [[-1]*m for _ in range(n)]

    for i in range(len(filed)):
        for j in range(len(filed[i])):
            if filed[i][j] == 0:
                result[i][j] = 0
            elif filed[i][j] == 2:
                que.append((i,j))
                result[i][j] = 0

    start = que[0]
    while que:
        x, y = que.popleft()

        for i, j in [(-1,0),(1,0),(0,-1),(0,1)]:
            nx, ny = x + i, y + j
            if 0 <= nx < n and 0 <= ny < m:
                if filed[nx][ny] == 1 and start != (nx, ny):
                    result[nx][ny] = result[x][y] + 1
                    que.append((nx, ny))
                    filed[nx][ny] = 0
    
    return result

if __name__ == "__main__":
    n, m = map(int, input().split())
    filed = [list(map(int, input().split())) for _ in range(n)]

    result = BFS(filed, n, m)
    for i in range(n):
        for j in range(m):
            print(result[i][j], end=' ')
        print()
