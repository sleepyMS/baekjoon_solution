import sys

def mrtest(b, t, n, s):
    x = pow(b, t, n)
    if x == 1:
        return True
    for i in range(s):
        if x == n - 1:
            return True
        x = pow(x, 2, n)
    return False


def isprime(n):
    if n < 2 or not n & 1 and n != 2:  # 홀수 판별
        return False
    if n == 2 or n == 7 or n == 61:
        return True

    s = 0
    t = n - 1
    num_list = [2,3,5,7,11,13,17]
    while not t & 1:
        s += 1
        t >>= 1
    for b in num_list:
        if not mrtest(b, t, n, s):
            return False
    return True


N = int(input())
count = 0

for _ in range(N):
    n = int(sys.stdin.readline())
    num = 2 * n + 1
    if isprime(num):
        count += 1

print(count)
