import sys
input = sys.stdin.readline

p = []
for _ in range(int(input())):
    p.append(tuple(map(int, input().split()))) 

result_dict = dict()
for t in p:
    count = 1
    for k in p:
        if k[0] > t[0] and k[1] > t[1]:
            count += 1
        result_dict[t] = count

result = []
for re in p:
    result.append(str(result_dict[re]))

print(' '.join(result))