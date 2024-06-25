from collections import deque
import sys
input = sys.stdin.readline


def dfs(n, m, tet, start):
    max_poly = 0
    que = deque([start])
    
    while que:
        
        for i in range(n):
            for j in range(m):
                pass


if __name__ == "__main__":
    n, m = map(int, input().split())
    tet = [list(map(int, input().split())) for _ in range(n)]
    result = 0
    
    for i in range(n):
        for j in range(m):
            result = max(result, dfs(n, m, tet, (i,j)))
    
    