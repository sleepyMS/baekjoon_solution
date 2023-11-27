import math

min, max = map(int, input().split())
gap = max - min + 1

resultArr = [1 for _ in range(gap)]

for i in range(2, int(max**0.5) + 1):
    tmp = math.ceil(min / (i**2))

    for j in range(tmp * (i**2), max+1, i**2):
        resultArr[j - min] = 0

print(sum(resultArr))



# min, max = map(int, input().split())
# tmp = set()

# for i in range(2, int(max**0.5 + 1)):
#     if i**2 not in tmp:
#         tmp.update(list(range(i**2, max+1, i**2)))

# result = 0
# for i in range(min, max+1):
#     if i not in tmp:
#         result += 1

# print(result)