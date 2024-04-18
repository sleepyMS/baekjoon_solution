from queue import deque
import sys
input = sys.stdin.readline


def BFS(a, b):
    visited = set()
    que = deque([(a, '')])
    while que:
        tmp, tmp2 = que.popleft()
        for c in ['D', 'S', 'L', 'R']:
            m = 0
            if c == 'D':
                m = (tmp*2) % 10000
            elif c == 'S':
                m = tmp-1 if tmp - 1 else 9999
            elif c == 'L':
                m = (tmp % 1000) * 10 + (tmp // 1000)
            elif c == 'R':
                n = tmp % 10
                m = (tmp // 10) + 1000 * (tmp % 10)
            
            if m not in visited:
                que.append((m, tmp2 + c))
                if m == b:
                    return tmp2 + c
                
        visited.add(tmp)


if __name__ == "__main__":
    for _ in range(int(input())):
        a, b = map(int, input().split())
        if a == b:
            print()
        else:
            c = BFS(a, b)
            print(''.join(c))