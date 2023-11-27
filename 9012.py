import sys
input = sys.stdin.readline

for _ in range(int(input())):
    vps = input().rstrip()
    a = len(vps)
    b = 0

    while a != b:
        b = a
        vps = vps.replace('()', '')
        a = len(vps)

    if a == 0:
        print('YES')
    else:
        print('NO')