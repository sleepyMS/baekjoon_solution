import sys
input = sys.stdin.readline

n, m, b = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
answer = sys.maxsize
idx = 0

for target in range(257):
    max_target, min_target = 0, 0
    for i in range(n):
        for j in range(m):

            if graph[i][j] >= target:
                max_target += graph[i][j] - target
            else:
                min_target += target - graph[i][j]

    if max_target + b >= min_target:
        if min_target + (max_target * 2) <= answer:
            answer = min_target + (max_target * 2)
            idx = target

print(answer, idx)