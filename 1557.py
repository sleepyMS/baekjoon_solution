k = int(input())
count = 2
lenArr = list()
countArr = list()

while count**2 - len(lenArr) <= k:
    countArr.append(count**2)
    for i in countArr:
        for j in range(count**2, (count+1)**2, i):
            if j not in lenArr:
                lenArr.append(j)
    
    count += 1

result = 0
for i in range(1, 1000000001):
    if i not in lenArr:
        result += 1
    if result == k:
        print(i)
        break