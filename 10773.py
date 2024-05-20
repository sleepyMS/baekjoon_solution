import sys
input = sys.stdin.readline

n = int(input())
arr = []

for _ in range(n):
    tmp = int(input())
    if tmp:
        arr.append(tmp)
    else:
        arr.pop()

print(sum(arr))


# n = int(input())
# b = [x[x[i][1]] if x[i][0] == 0 else x[i] for i, x in enumerate([[b for b in [[int(input()), a] for a in (range(n))]]] * n)]


# print(b)