import sys
input = sys.stdin.readline


while True:
    tmp = list(input().rstrip())
    if tmp[0] == '0':
        break

    check = True
    while len(tmp) > 1:
        if tmp.pop(0) != tmp.pop():
            check = False
            break

    if check:
        print('yes')
    else:
        print('no')
