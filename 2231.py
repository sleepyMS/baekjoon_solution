n = int(input())
len_n = len(str(n))

m = n - len_n * 9
if m < 1:
    m = 1

for i in range(m, n):
    tmp = i
    tmpArr = []
    for _ in range(len_n):
        tmpArr.append(tmp % 10)
        tmp //= 10
    
    if i + sum(tmpArr) == n:
        print(i)
        break

else:
    print(0)