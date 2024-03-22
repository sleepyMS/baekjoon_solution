n, k = map(int, input().split())

filed = [100001] * (k + n)
for i in range(n+1):
    filed[i] = n - i

for i in range(n+1, k+n):
    if i % 2 == 0:
        filed[i] = min(filed[i//2]+1, filed[i-1]+1)


        # for j in range(i-1, i//2 + i//4, -1):
        #     filed[j] = min(filed[j+1]+1, filed[j])
        
    else:
        filed[i] = filed[i-1] + 1

    # print(filed)

print(filed[k])

for i in range(n, n + k):
    for j in range()