import sys
input = sys.stdin.readline


def DFS(color, n, first, check):
    global a_visited, b_visited
    stack = [first]
    load = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    while stack:
        x, y = stack.pop()
        
        if check:
            for r, c in load:
                nx = x + r
                ny = y + c
                if 0 <= nx < n and 0 <= ny < n:
                    if color[nx][ny] == color[x][y] and (nx, ny) not in a_visited:
                        stack.append((nx, ny))
                        a_visited.add((nx, ny))
        else:
            for r, c in load:
                nx = x + r
                ny = y + c
                if 0 <= nx < n and 0 <= ny < n:
                    if (nx, ny) not in b_visited:
                        if color[x][y] == 'R' or color[x][y] == 'G':
                            if color[nx][ny] == 'R' or color[nx][ny] == 'G':
                                stack.append((nx, ny))
                                b_visited.add((nx, ny))
                        elif color[nx][ny] == color[x][y]:
                            if color[nx][ny] == color[x][y]:
                                stack.append((nx, ny))
                                b_visited.add((nx, ny))
                                
                                
if __name__ == "__main__":
    n = int(input())
    color = [input().rstrip() for _ in range(n)]
    a, b = 0, 0
    a_visited, b_visited = set(), set()
    
    for i in range(n):
        for j in range(n):
            if (i, j) not in a_visited:
                DFS(color, n, (i, j), True)
                a_visited.add((i, j))
                a += 1
            if (i, j) not in b_visited:
                DFS(color, n, (i, j), False)
                b_visited.add((i, j))
                b += 1
    
    print(a, b)