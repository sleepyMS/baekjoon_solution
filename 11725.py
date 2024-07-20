from collections import deque
import sys
input = sys.stdin.readline


def dfs(graph, n, start=1):
    que = deque([start])
    visited = set()
    result = {i: 0 for i in range(1, n+1)}
    
    while que:
        tmp = que.popleft()
        if tmp in visited:
            continue
        visited.add(tmp)
        
        for i in graph[tmp]:
            if not result[i]:
                result[i] = tmp
            que.append(i)
    
    del result[1]
    return result


if __name__ == "__main__":
    n = int(input())
    tmp = [map(int, input().split()) for _ in range(n-1)]
    graph = {i: [] for i in range(1, n+1)}

    for i, j in tmp:
        graph[i].append(j)
        graph[j].append(i)
    
    for i in dfs(graph, n).values():
        print(i)
