import sys
input = sys.stdin.readline

n = int(input())
net = [[0] * n for _ in range(n)]
for _ in range(int(input())):
    a, b = map(int, input().split())
    net[a-1][b-1], net[b-1][a-1] = 1, 1
