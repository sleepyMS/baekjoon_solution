a = input()
b = input()
dp = [[0] * (len(a)+1) for _ in range(len(b)+1)]

for i, t1 in enumerate(b, start=1):
    for j, t2 in enumerate(a, start=1):
        if t1 == t2:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
            
print(max(max(dp)))