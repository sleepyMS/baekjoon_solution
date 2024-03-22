import sys
input = sys.stdin.readline
EPS = 1e-9

tmpArr = []
for _ in range(int(input())):
    tmpArr.append(int(input()))

tmpArr = sorted(tmpArr, key=lambda x : x)
lenArr = round(len(tmpArr) * 0.15 + EPS)
result = []
if lenArr > 0:
    result = tmpArr[lenArr:-lenArr]
else:
    result = tmpArr

if len(result):
    print(round(sum(result) / len(result) + EPS))
else:
    print(0)