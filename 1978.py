n = int(input())
cnt = 0

for i in map(int, input().split()):
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            break
    else:
        if i > 1:
            cnt += 1

print(cnt)