import sys
input = sys.stdin.readline


def DFS(graph, a):
    global visited
    
    stack = [a]
    while stack:
        tmp = stack.pop()
        if tmp not in visited:
            visited.add(tmp)
            stack.extend(graph[tmp])
            
    
if __name__ == "__main__":
    n, m = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    visited = set()
    cnt = 0
    
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    for i in range(1, n+1):
        if i in visited:
            continue
        else:
            DFS(graph, i)
            cnt += 1
            
    print(cnt)
    
    