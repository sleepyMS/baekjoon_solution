# kmp로직

# def compute_pi(pattern):
#     m = len(pattern)
#     pi = [0] * m
#     k = 0
#     for q in range(1, m):
#         while k > 0 and pattern[k] != pattern[q]:
#             k = pi[k - 1]
#         if pattern[k] == pattern[q]:
#             k += 1
#         pi[q] = k
#     return pi

# def kmp(n, m, s):
#     result = 0
#     pattern = ['I' if i % 2 == 0 else 'O' for i in range(2*n+1)]
#     pi = compute_pi(pattern)
    
#     current = 0
#     while current + 2*n + 1 <= m:
#         match = True
#         for i in range(2*n+1):
#             if s[current+i] != pattern[i]:
#                 match = False
#                 current += i - pi[i - 1] if i > 0 else 1
#                 break
#         if match:
#             result += 1
#             current += 1
            
#     return result

# if __name__ == "__main__":
#     n = int(input())
#     m = int(input())
#     s = input().rstrip()
    
#     print(kmp(n, m, s))

##########################################

N = int(input())
M = int(input())
S = input()

count = 0
pattern = 0
i = 1
while i < M-1:
    if S[i-1] == 'I' and S[i] == 'O' and S[i+1] == 'I':
        pattern += 1
        if pattern == N:
            pattern -= 1
            count += 1   
        i += 1
    else:
        pattern = 0
    i += 1
    
print(count)

