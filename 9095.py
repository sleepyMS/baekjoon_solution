import math
import sys
input = sys.stdin.readline


if __name__ == "__main__":
    nArr = [int(input()) for _ in range(int(input()))]
    result = [0,1,2,4] + [0 for _ in range(max(nArr) - 3)]

    for i in range(4, len(result)):
        result[i] = result[i-1] + result[i-2] + result[i-3]
    
    for i in nArr:
        print(result[i])

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

