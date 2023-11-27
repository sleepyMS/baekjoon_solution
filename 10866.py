from collections import deque
import sys
input = sys.stdin.readline

num = deque()
for i in range(int(input())):
    cmd = input().rstrip() 
    if 'push_front' in cmd:
        num.appendleft(int(cmd.split()[-1]))
    elif 'push_back' in cmd:
        num.append(int(cmd.split()[-1]))
    elif cmd == 'pop_front':
        print(-1) if len(num) == 0 else print(num.popleft())
    elif cmd == 'pop_back':
        print(-1) if len(num) == 0 else print(num.pop())
    elif cmd == 'size':
        print(len(num))
    elif cmd == 'empty':
        print(1) if len(num) == 0 else print(0)
    elif cmd == 'front':
        print(-1) if len(num) == 0 else print(num[0])
    elif cmd == 'back':
        print(-1) if len(num) == 0 else print(num[-1])