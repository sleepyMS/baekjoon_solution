import sys
input = sys.stdin.readline

n, m = map(int, input().split())

arr = list(map(int, input().split()))
max = -1
# nums = []
for i in range(0, n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            num = arr[i]+arr[j]+arr[k]
            if num > max and m >= num:
                max = num

print(max)