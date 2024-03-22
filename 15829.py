l = int(input())
s = input()

numArr = []
for i in s:
    numArr.append(ord(i) - 96)

result = []
for i, a in enumerate(numArr):
    result.append(a*pow(31,i))

print(sum(result) % 1234567891)