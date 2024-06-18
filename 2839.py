# n = int(input())

# if n == 7 or n == 4:
#     print(-1)
# else:
#     five = n // 5
#     tmp = n % 5
#     while True:
#         if tmp % 3 == 0:
#             print(five + (tmp // 3))
#             break
#         else:
#             five -= 1
#             tmp += 5

n = int(input())
dp = [-1, -1, -1, 1, -1, 1, 2, -1, 2, 3] + [-1]*n

for i in range(n+1):
    if i != -1:
        dp[i] = dp[i-3] + 1
        dp[i] = dp[i-5] + 1
        
        dp[i] = min(dp[i-3] + 1, dp[i-5] + 1)
    
print(dp[n])
