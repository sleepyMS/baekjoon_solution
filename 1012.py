import sys
input = sys.stdin.readline


## 재귀를 사용한 DFS
# def DFS(arr, row, col, N, M):
#     if arr[row][col] == 1:
#         arr[row][col] = 0
#         for di, dj in [[0,1],[0,-1],[1,0],[-1,0]]:
#             ni = row + di
#             nj = col + dj
#             if 0 <= ni < N and 0 <= nj < M:
#                 DFS(arr, ni, nj, N, M)
#         return 1
#     return 0

# 스택을 활용한 DFS
def DFS(arr, row, col, N, M):
    stack = [[row, col]]
    while stack:
        i, j = stack.pop()
        arr[i][j] = 0
        for di, dj in [[0,1], [0,-1], [1,0], [-1,0]]:
            ni = i + di
            nj = j + dj
            if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] == 1:
                stack.append([ni, nj])
    return 1

def solve():
    M, N, K = map(int, input().split())
    field = [[0] * M for _ in range(N)]
    for _ in range(K):
        X, Y = map(int, input().split())
        field[Y][X] = 1

    earthworm = 0
    for i in range(N):
        for j in range(M):
            if field[i][j] == 1:
                earthworm += DFS(field, i, j, N, M)
    return earthworm


for _ in range(int(input())):
    print(solve())

