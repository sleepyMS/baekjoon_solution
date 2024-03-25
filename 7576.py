from queue import deque
import sys
input = sys.stdin.readline


def BFS(filed, m, n):
    que = deque([])
    count = 0
    for i in range(len(filed)):
        for j in range(len(filed[i])):
            if filed[i][j] == 1:
                que.append((i,j))

    while que:
        x, y = que.popleft()
        for i, j in [(-1,0),(0,-1),(1,0),(0,1)]:
            nx, ny = x + i, y + j
            if 0 <= nx < n and 0 <= ny < m:
                if filed[nx][ny] == 0:
                    filed[nx][ny] = filed[x][y] + 1
                    que.append((nx, ny))
    
    result = 0
    for i in filed:
        for j in i:
            if j == 0:
                return -1
            elif j > result:
                result = j

    return result - 1


if __name__ == "__main__":
    m, n = map(int, input().split())
    filed = []
    for _ in range(n):
        filed.append(list(map(int, input().split())))

    print(BFS(filed, m, n))
