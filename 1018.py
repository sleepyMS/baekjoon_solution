import itertools
import sys
input = sys.stdin.readline


chess_1 = list("WBWBWBWBBWBWBWBWWBWBWBWBBWBWBWBWWBWBWBWBBWBWBWBWWBWBWBWBBWBWBWBW")
chess_2 = list("BWBWBWBWWBWBWBWBBWBWBWBWWBWBWBWBBWBWBWBWWBWBWBWBBWBWBWBWWBWBWBWB")

a, b = map(int, input().split())
arr = []

for i in range(a):
    arr.append(list(''.join(input())))

check = []
for i in range(a-7):
    for j in range(b-7):

        arr_check = []
        for k in range(8):
            arr_check.append(arr[i+k][j:j+8])
            arr_check = list(itertools.chain(*arr_check))

        result = 0
        for k in range(64):
            if chess_1[k] != arr_check[k]:
                result += 1
        check.append(result)
        result = 0
        for k in range(64):
            if chess_2[k] != arr_check[k]:
                result += 1
        check.append(result)

print(min(check))
