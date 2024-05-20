# import sys
# input = sys.stdin.readline

# for _ in range(int(input())):
#     n = int(input())
#     mbti = [set(m) for m in input().rstrip().split()]
#     if n > 32:
#         print(0)
#         continue
    
#     result = 8
#     for a in range(n-2):
#         for b in range(a+1, n-1):
#             for c in range(b+1, n):
#                 tmp = len(mbti[a] - mbti[b]) + len(mbti[a] - mbti[c]) + len(mbti[b] - mbti[c])
#                 result = min(result, tmp)
                
#     print(result)
    
    
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    mbti = [set(m) for m in input().rstrip().split()]
    if n > 32:
        print(0)
        continue
    
    arr = [len(mbti[a] - mbti[b]) + len(mbti[a] - mbti[c]) + len(mbti[b] - mbti[c]) for a in range(n-2) for b in range(a+1, n-1) for c in range(b+1, n)]
                
    print(min(arr))
    