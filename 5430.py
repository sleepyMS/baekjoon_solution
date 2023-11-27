from collections import deque
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    command = input()
    dq = []
    if int(input()):
        dq = deque(map(int, input().rstrip()[1:-1].split(',')))
    else:
        tmp = input()
        dq = deque([])

    count = 0
    for c in command:
        if not len(dq) and c == 'D':
            print('error')
            break
        if c == 'R':
            count += 1
        elif c == 'D':
            if count % 2 == 0:
                dq.popleft()
            else:
                dq.pop()
    else:
        if count % 2 == 1:
            dq.reverse()
        
        print('[' + ','.join(map(str, dq)) + ']')