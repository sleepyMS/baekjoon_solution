import sys
input = sys.stdin.readline

n = int(input())
s = set()

while n:
    tmp = input().split()
    if tmp[0] == "all" or tmp[0] == "empty":
        s = set([i for i in range(1, 21)])
        if tmp[0] == "empty":
            s = set()
    else:
        m = int(tmp[1])
        if tmp[0] == "add":
            s.add(m)
        elif tmp[0] == "remove":
            if m in s:
                s.remove(m)
        elif tmp[0] == "check":
            if m in s:
                print(1)
            else:
                print(0)
        elif tmp[0] == "toggle":
            if m in s:
                s.remove(m)
            else:
                s.add(m)
                
    n -= 1