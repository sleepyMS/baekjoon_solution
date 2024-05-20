import sys
input = sys.stdin.readline

n, m = map(int, input().split())
site = {k: v for _ in range(n) for k, v in [input().split()]}
for _ in range(m):
    print(site[input().rstrip()])