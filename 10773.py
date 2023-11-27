import sys
input = sys.stdin.readline

testCase = int(input())
moneyCheck = list()
for _ in range(testCase):
    tmp = int(input())
    if tmp == 0:
        moneyCheck.pop()
    else:
        moneyCheck.append(tmp)

print(sum(moneyCheck))