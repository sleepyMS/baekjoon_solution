n = int(input())
m = [0] * (n + 1)
m[1], m[2], m[3] = 1, 2, 3
for i in range(int(n**(1/2)) + 1):
    m[i**2] = 1
    for j, k in enumerate(range(i**2, n)):
        pass


for i in range(n+1):
    pass


# i = int(n**(1/2))
# result = 0
# while n != 0:
#     if n >= i**2:
#         n -= i**2
#         result += 1
#         print(n, i)

#     if n < 4:
#         result += n
#         break
#     else:
#         i -= 1

# print(result)