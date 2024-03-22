def combination(n, r):
    if n == r:
        return 1
    elif n < r:
        n, r = r, n

    tmp = 1
    for i in range(n, n-r, -1):
        tmp *= i

    print(tmp // r)

    return tmp // r


n = int(input())

if n == 1:
    print(1)
else:
    m = n // 2
    result = 1
    for i in range(1, m+1):
        print(i, result)
        result += combination(n - i*2 + 1, i)

    print(result)
        
    