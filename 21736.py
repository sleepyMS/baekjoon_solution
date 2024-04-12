from queue import deque
import sys
input = sys.stdin.readline


def BFS(filed):
    global n, m
    cnt = 0
    
    load = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    que = deque([(i, j) for i in range(n) for j in range(m) if filed[i][j] == 'I'])
    visited = set(que)
    while que:
        x, y = que.popleft()
        for i, j in load:
            nx, ny = x + i, y + j
            if 0 <= nx < n and 0 <= ny < m and filed[nx][ny] != 'X' and (nx, ny) not in visited:
                que.append((nx, ny))
                visited.add((nx, ny))
                if filed[nx][ny] == 'P':
                    cnt += 1
    return cnt
    

if __name__ == "__main__":
    n, m = map(int, input().split())
    filed = [input() for _ in range(n)]
    tmp = BFS(filed)
    
    if tmp:
        print(tmp)
    else:
        print('TT')
    