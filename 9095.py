import sys
input = sys.stdin.readline

nArr = [int(input()) for _ in range(int(input()))]
dp = [0,1,2,4] + [0]*(max(nArr) - 3)

for i in range(4, len(dp)):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

for i in nArr:
    print(dp[i])


# import math
# import sys
# input = sys.stdin.readline

# # 중복조합 이용
# def combinationReplace(n, r):
#     n = n + r - 1
#     re = 1
#     for i in range(n, n-r, -1):
#         re *= i

#     return re // math.factorial(r)

# for _ in range(int(input())):
#     n = int(input())
#     count = 0

#     for i in range(n//3 + 1):
#         for j in range((n - 3*i)//2 + 1):
#             count += combinationReplace(n - 3*i - 2*j + 1, i) * combinationReplace(n - 2*i - 2*j + 1, j)

#     print(count)

