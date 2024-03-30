import sys
input = sys.stdin.readline

def paper(filed, n):
    result = [[1,0], [0,1]]
    if n == 1:
        return result[filed[0][0]]
    else:
        color = 0
        for i in range(n):
            for j in range(n):
                if i == 0 and j == 0:
                    color = filed[0][0]
                if filed[i][j] != color:
                    tmp = n // 2
                    a, b, c, d = [], [], [], []
                    for arr in filed[:tmp]:
                        a.append(arr[:tmp])
                        b.append(arr[tmp:])                        
                    for arr in filed[tmp:]:
                        c.append(arr[:tmp])
                        d.append(arr[tmp:])
                    return paper(a, tmp) + paper(b, tmp) + paper(c, tmp) + paper(d, tmp)
        else:
            return result[color]
        

if __name__ == "__main__":
    n = int(input())
    filed = [list(map(int, input().split())) for _ in range(n)]
    
    white = 0
    blue = 0
    for i, c in enumerate(paper(filed, n)):
        if i % 2 == 0:
            white += c
        else:
            blue += c
            
    print(white)
    print(blue)

##########################################################################################################################

# import numpy as np
# import sys
# input = sys.stdin.readline

# def paper(filed, n):
#     result = np.array([[1,0], [0,1]])
#     if n == 1:
#         return result[filed[0][0]]
#     else:
#         color = 0
#         for i in range(n):
#             for j in range(n):
#                 if i == 0 and j == 0:
#                     color = filed[0][0]
#                 if filed[i][j] != color:
#                     tmp = n // 2
#                     return paper(filed[:tmp][:,:tmp], tmp) + paper(filed[:tmp][:,tmp:], tmp) + paper(filed[tmp:][:,tmp:], tmp) + paper(filed[tmp:][:,:tmp], tmp)
#         else:
#             return result[color]
        

# if __name__ == "__main__":
#     n = int(input())
#     filed = np.array([list(map(int, input().split())) for _ in range(n)])
    
#     for i in paper(filed, n):
#         print(i)

