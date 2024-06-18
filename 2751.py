import sys
input = sys.stdin.readline

[print(s) for s in sorted([int(input()) for _ in range(int(input()))])]