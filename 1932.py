import sys
input = sys.stdin.readline

n = int(input())
tree = [list(map(int, input().rstrip().split())) for _ in range(n)]

dp = [[tree[0][0]] if i == 1 else [0]*i for i in range(1, n+1)]

for flo in tree:
    for i, j in enumerate(flo):
        
