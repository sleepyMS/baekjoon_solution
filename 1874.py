from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
stack = []
result = []
done = False
current = 1
for _ in range(n):
    num = int(input())
    
    while True:
        if current > n + 1:
            done = True
            break

        if len(stack) == 0:
            stack.append(current)
            result.append('+')
            current += 1
        elif stack[-1] == num:
            stack.pop()
            result.append('-')
            break
        else:
            stack.append(current)
            result.append('+')
            current += 1

if done:
    print("NO")
else:
    print('\n'.join(result))