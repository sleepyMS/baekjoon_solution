from queue import deque
import sys
input = sys.stdin.readline


def BFS(ladder, snake):
    que = deque([(1, 0)])
    visited = set([1])
    
    while que:
        current, cnt = que.popleft()
        if current == 100:
            return cnt
        
        for i in range(1, 7):
            next = current + i
            if next in ladder:
                next = ladder[next]
            if next in snake:
                next = snake[next]
            if next not in visited:
                que.append((next, cnt + 1))
                visited.add(next)
        

if __name__ == "__main__":
    n, m = map(int, input().split())
    ladder = {i: j for _ in range(n) for i, j in [tuple(map(int, input().split()))]}
    snake = {i: j for _ in range(m) for i, j in [tuple(map(int, input().split()))]}
    print(BFS(ladder, snake))

