a, b = map(int, input().split())
m = max(a, b)
resultA, resultB = 0, 0

for i in range(m):
    if m % (m - i) == 0:
        if min(a, b) % (m - i) == 0:
            resultA = m - i
            resultB = a * b // resultA
            break

print(resultA)
print(resultB)