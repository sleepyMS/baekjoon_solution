import sys
input = sys.stdin.readline

num = list()
for i in range(int(input())):
    cmd = input().rstrip() 
    if 'push' in cmd:
        num.append(int(cmd.split()[-1]))
    elif cmd == 'pop':
        print(-1) if len(num) == 0 else print(num.pop())
    elif cmd == 'size':
        print(len(num))
    elif cmd == 'empty':
        print(1) if len(num) == 0 else print(0)
    elif cmd == 'top':
        print(-1) if len(num) == 0 else print(num[-1])