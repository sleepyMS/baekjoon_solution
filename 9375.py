import sys
input = sys.stdin.readline

for _ in range(int(input())):
    dict_n = {}
    for __ in range(int(input())):
        tmp = input().split()

        if tmp[1] in dict_n:
            dict_n[tmp[1]].append(tmp[0])
        else:
            dict_n[tmp[1]] = [tmp[0]]

    s = 1
    for i in dict_n.values():
        s *= len(i) + 1

    print(s - 1)
