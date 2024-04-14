from queue import deque
import sys
input = sys.stdin.readline


def BFS(graph, n, start):
    que = deque([start])
    graph[start[0]][start[1]] = 0
    cnt = 1
    
    while que:
        x, y = que.popleft()
        for i, j in [(-1, 0), (1, 0), (0,-1), (0, 1)]:
            nx, ny = x + i, y + j
            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny]:
                que.append((nx, ny))
                graph[nx][ny] = 0
                cnt += 1
    
    return cnt

if __name__ == "__main__":
    n = int(input())
    graph = [list(map(int, input().rstrip())) for _ in range(n)]
    result = [BFS(graph, n, (i,j)) for i in range(n) for j in range(n) if graph[i][j]]
    print(len(result))
    for i in sorted(result):
        print(i)
    