from collections import deque

def bfs(load, n, m, start):
    que = deque([(start, 0, 1)])
    tmp = {}
    visited = set()
    
    while que:
        cur = que.popleft()
        
        if cur[0] in visited:
            if tmp[cur[0]][0] == cur[1] and tmp[cur[0]][1] <= cur[2]:
                continue
        elif cur[0] == (n-1, m-1):
            return cur[2]
        tmp[cur[0]] = (cur[1], cur[2])
        visited.add(cur[0])
        
        for x, y in [[-1, 0], [0, -1], [1, 0], [0, 1]]:
            dx, dy = cur[0][0]+x, cur[0][1]+y
            
            if 0 <= dx < n and 0 <= dy < m:
                if load[dx][dy] == 1 and cur[1] == 0:
                    que.append(((dx, dy), cur[1]+1, cur[2]+1))
                elif load[dx][dy] == 0:
                    que.append(((dx, dy), cur[1], cur[2]+1))
    
    return -1
    

if __name__ == "__main__":
    n, m = map(int, input().split())

    load = [list(map(int, list(input()))) for _ in range(n)]
    result = bfs(load, n, m, (0,0))
    print(result)
    
    