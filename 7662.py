from heapq import heappush, heappop
import sys
input = sys.stdin.readline


for _ in range(int(input())):
    max_heap, min_heap, tmp_max, tmp_min = [], [], set(), set()

    for __ in range(int(input())):
        arg = input().rstrip()

        if arg == "D 1":
            if max_heap != []:
                tmp = heappop(max_heap)
                tmp_max.add(-tmp)
                
                if max_heap == [] or -max_heap[0] < min_heap[0]:
                    max_heap, min_heap, tmp_max, tmp_min = [], [], set(), set()
                if len(min_heap) and -tmp == min_heap[0]:
                    heappop(min_heap)
                    tmp_max.remove(-tmp)
                    if not len(min_heap):
                        max_heap, min_heap, tmp_max, tmp_min = [], [], set(), set()
                while max_heap[0] in tmp_min:
                    tmp = heappop(max_heap)
                    tmp_min.remove(tmp)
        elif arg == "D -1":
            if min_heap != []:
                tmp = heappop(min_heap)
                tmp_min.add(-tmp)
                if min_heap == [] or -max_heap[0] < min_heap[0]:
                    max_heap, min_heap, tmp_max, tmp_min = [], [], set(), set()
                if len(max_heap) and -tmp == max_heap[0]:
                    heappop(max_heap)
                    tmp_min.remove(-tmp)
                    if not len(max_heap):
                        max_heap, min_heap, tmp_max, tmp_min = [], [], set(), set()
                while min_heap[0] in tmp_max:
                    tmp = heappop(min_heap)
                    tmp_max.remove(tmp)
        else:
            num = int(arg[2:])
            heappush(max_heap, -num)
            heappush(min_heap, num)
        

    if min_heap == [] and max_heap == []:
        print("EMPTY")
    elif max_heap != [] and min_heap == []:
        print(-max_heap[0], -max_heap[0])
    elif max_heap == [] and min_heap != []:
        print(min_heap[0], min_heap[0])
    else:
        print(-heappop(max_heap), heappop(min_heap))