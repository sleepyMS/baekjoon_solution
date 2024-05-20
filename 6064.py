import sys
input = sys.stdin.readline

for _ in range(int(input())):
    m, n, x, y = map(int, input().split())
    end = m * n
    nx = {i for i in range(x, end + 1, m)}
    
    for i in [i for i in range(y, end + 1, n)]:
        if i in nx:
            print(i)
            break
    else:
        print(-1)