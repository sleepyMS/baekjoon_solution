# import sys
# input = sys.stdin.readline

# n = int(input())
# load = [list(map(int, input().split())) for _ in range(n)]
# dp_min = [[0]*3 for _ in range(n)]
# dp_max = [[0]*3 for _ in range(n)]

# dp_min[0], dp_max[0] = load[0], load[0]
# for i in range(1, n):
#     dp_min[i][0] = min(dp_min[i-1][0], dp_min[i-1][1]) + load[i][0]
#     dp_min[i][1] = min(dp_min[i-1][0], dp_min[i-1][1], dp_min[i-1][2]) + load[i][1]
#     dp_min[i][2] = min(dp_min[i-1][1], dp_min[i-1][2]) + load[i][2]
    
#     dp_max[i][0] = max(dp_max[i-1][0], dp_max[i-1][1]) + load[i][0]
#     dp_max[i][1] = max(dp_max[i-1][0], dp_max[i-1][1], dp_max[i-1][2]) + load[i][1]
#     dp_max[i][2] = max(dp_max[i-1][1], dp_max[i-1][2]) + load[i][2]

# print(str(max(dp_max[-1])) + ' ' + str(min(dp_min[-1])))



import sys
input = sys.stdin.readline

n = int(input())
load = [list(map(int, input().split())) for _ in range(n)]

dp_min_prev, dp_max_prev = load[0][:], load[0][:]
for i in range(1, n):
    tmp_min1 = min(dp_min_prev[0], dp_min_prev[1]) + load[i][0]
    tmp_min2 = min(dp_min_prev[0], dp_min_prev[1], dp_min_prev[2]) + load[i][1]
    tmp_min3 = min(dp_min_prev[1], dp_min_prev[2]) + load[i][2]
    
    tmp_max1 = max(dp_max_prev[0], dp_max_prev[1]) + load[i][0]
    tmp_max2 = max(dp_max_prev[0], dp_max_prev[1], dp_max_prev[2]) + load[i][1]
    tmp_max3 = max(dp_max_prev[1], dp_max_prev[2]) + load[i][2]
    
    dp_min_prev = [tmp_min1, tmp_min2, tmp_min3]
    dp_max_prev = [tmp_max1, tmp_max2, tmp_max3]

print(f"{max(dp_max_prev)} {min(dp_min_prev)}")
