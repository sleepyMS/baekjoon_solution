import sys
input = sys.stdin.readline

N = int(input())
rgb = [list(map(int, input().rstrip().split())) for _ in range(N)]
dp = [[0]*3 for _ in range(N+1)]

for i in range(1, N+1):
    dp[i][0] = min(dp[i-1][1],dp[i-1][2]) + rgb[i-1][0]
    dp[i][1] = min(dp[i-1][0],dp[i-1][2]) + rgb[i-1][1]
    dp[i][2] = min(dp[i-1][0],dp[i-1][1]) + rgb[i-1][2]
    
print(min(dp[-1]))