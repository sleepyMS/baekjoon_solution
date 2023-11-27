from collections import deque

n = int(input())
de = deque([i for i in range(1, n+1)])

while len(de) > 1:
    de.popleft()
    de.append(de.popleft())

print(de[0])