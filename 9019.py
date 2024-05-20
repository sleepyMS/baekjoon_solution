from collections import deque
import sys

input = sys.stdin.readline

def BFS(a, b):
    que = deque([(a, '')])
    visited = set([a])
    
    while que:
        current, path = que.popleft()
        
        if current == b:
            return path
        
        m = (current * 2) % 10000
        if m not in visited:
            visited.add(m)
            que.append((m, path + 'D'))
        
        m = current - 1 if current != 0 else 9999
        if m not in visited:
            visited.add(m)
            que.append((m, path + 'S'))
        
        m = (current % 1000) * 10 + (current // 1000)
        if m not in visited:
            visited.add(m)
            que.append((m, path + 'L'))
        
        m = (current // 10) + 1000 * (current % 10)
        if m not in visited:
            visited.add(m)
            que.append((m, path + 'R'))

if __name__ == "__main__":
    for _ in range(int(input())):
        a, b = map(int, input().split())
        print(BFS(a, b))