def Z(n, r, c):
    tmp = pow(2, n-1)
    r_n = r // tmp
    c_n = c // tmp
    result_n = (r_n * 2 + c_n) * pow(tmp, 2)

    if n == 1:
        return result_n

    r %= tmp
    c %= tmp

    return result_n + Z(n-1, r, c)


n, r, c = map(int, input().split())
print(Z(n, r, c))