import sys
input = sys.stdin.readline

team = [tuple(map(int, input().split())) for _ in range(int(input()))]

team = sorted(team, key=lambda x: (x[1], x[0]))
start, result = 0, 0
for x, y in team:
    if x < start:
        continue
    start = y
    result += 1

print(result)