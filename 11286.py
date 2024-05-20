from queue import PriorityQueue
import sys
input = sys.stdin.readline

que = PriorityQueue()
for _ in range(int(input())):
    tmp = int(input())
    if tmp:
        que.put((abs(tmp), tmp))
    elif que.empty():
        print(0)
    else:
        print(que.get()[1])
