import sys
from collections import deque
input = sys.stdin.readline


def DFS(g, v):
    visited = []
    stack = [v]

    while stack:
        current = stack.pop()
        if current not in visited:
            visited.append(current)
            stack += sorted(g[current] - set(visited), reverse=True)

    return visited


def BFS(g, v):
    visited = []
    queue = deque([v])

    while queue:
        n = queue.popleft()
        if n not in visited:
            visited.append(n)
            queue += sorted(g[n] - set(visited))

    return visited


n, m, v = map(int, input().split())
f = {i: set() for i in range(1, n+1)}
for _ in range(m):
    a, b = map(int, input().split())
    f[a].add(b)
    f[b].add(a)

print(' '.join(map(str, DFS(f, v))))
print(' '.join(map(str, BFS(f, v))))

