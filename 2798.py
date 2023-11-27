n, m = map(int, input().split())
card = list(map(int, input().split()))

result = []
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            result.append(card[i] + card[j] + card[k])

result = sorted(result)
for i, num in enumerate(result):
    if num > m:
        print(result[i-1])
        break
else:
    print(result[-1])