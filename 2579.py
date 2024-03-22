import sys
input = sys.stdin.readline

n = int(input())
step = [0]*(n+3)
a = [0]*(n+3)

for i in range(1,n+1):
    step[i] = int(input())

a[1] = step[1]
a[2] = step[1]+step[2]
a[3] = max(step[1]+step[3],step[2]+step[3])
for i in range(4,n+1):
    a[i] = max(a[i-2]+step[i], a[i-3]+step[i-1]+step[i])
print(a[n])