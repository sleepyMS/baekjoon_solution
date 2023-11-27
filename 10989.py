import sys
input = sys.stdin.readline

n = int(input())
sortArray = [0 for _ in range(10001)]

for _ in range(n):
    sortArray[int(input())] += 1

for i in range(1, 10001):
    if sortArray[i]:
        for _ in range(sortArray[i]):
            print(i)