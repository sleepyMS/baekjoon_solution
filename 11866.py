from collections import deque

n, k = map(int, input().split())

de = deque([i for i in range(1, n+1)])
tmp = list()
while len(de):
    de.rotate(-(k-1))
    tmp.append(de.popleft())

s = ", ".join(map(str, tmp))
print('<'+s+'>')