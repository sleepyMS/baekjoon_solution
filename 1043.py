from collections import deque
import sys
input = sys.stdin.readline


def bfs(graph, n, m, start):
    que = deque(start)
    visited = set()
    result = {i: 0 for i in range(1, n+1)}
    for i in start:
        result[i] = 1
        
    while que:
        tmp = que.popleft()
        if tmp in visited:
            continue
        visited.add(tmp)
        
        for i in graph[tmp]:
            que.append(i)
            result[i] = 1
    
    return set([k for k, v in result.items() if v])


if __name__ == "__main__":
    n, m = map(int, input().split())
    p = list(map(int, input().split()))
    party = [set(list(map(int, input().split()))[1:]) for _ in range(m)]
    cnt = 0
    
    if p[0] == 0:
        print(m)
    else:
        p = p[1:]
        graph = {i: set() for i in range(1, n+1)}
        for i in party:
            for j in i:
                for k in i:
                    graph[j].add(k)
        
        for i in range(1, n+1):
            graph[i].discard(i)
            
        result = bfs(graph, n, m, p)

        for i in range(m):
            if party[i] ==  party[i] - result:
                cnt += 1
        
        print(cnt)
