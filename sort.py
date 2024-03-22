def findMinIdx(ary):
    minIdx = 0
    for i in range(1, len(ary)):
        if (ary[minIdx] > ary[i]):
            minIdx = i
    return minIdx

def selectionSort(ary):
    n = len(ary)
    for i in range(0, n-1):
        minIdx = i
        for k in range(i+1, n):
            if (ary[minIdx] > ary[k]):
                minIdx = k
        
        tmp = ary[i]
        ary[i] = ary[minIdx]
        ary[minIdx] = tmp
    return ary

def findInsertIdx(ary, data):
    findIdx = -1
    for i in range(0, len(ary)):
        if (ary[i] > data):
            findIdx = i
            break
    if findIdx == -1:
        return len(ary)
    else:
        return findIdx


testAry = [55,88,33,77]
minPos = findMinIdx(testAry)
print('최솟값 -->', testAry[minPos])

dataAry = [188,162,168,120,50,150,177,105]

print('정렬 전 -->', dataAry)
dataAry = selectionSort(dataAry)
print('정렬 후 -->', dataAry)


before = [188,162,168,120,50,150,177,105]
after = []

print('정렬 전 -->', before)
for _ in range(len(before)):
    minPos = findMinIdx(before)
    after.append(before[minPos])
    del(before[minPos])
print('정렬 후 -->', after)


testAry = []
insPos = findInsertIdx(testAry, 55)
print('삽입할 위치 -->', insPos)

testAry = [33,77,88]
insPos = findInsertIdx(testAry, 55)
print('삽입할 위치 -->', insPos)

testAry = [33,55,77,88]
insPos = findInsertIdx(testAry, 100)
print('삽입할 위치 -->', insPos)
