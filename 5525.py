import sys
input = sys.stdin.readline

def KMP(s):
    global n, m, s, len_s, n_s
    result = 0

    lps = [0] * len_s
    j = 0 # pat[]의 인덱스
 
    # lps[] 배열을 계산합니다.
    computeLPSArray(pat, M, lps)

    return result


def computeLPSArray(pat, M, lps):
    length = 0 # 이전 가장 긴 접미사의 길이
 
    lps[0] = 0 # lps[0]은 항상 0
    i = 1
 
    # lps[i]를 계산
    while i < M:
        if pat[i]== pat[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            # (pat[i] != pat[len])
            if length != 0:
                length = lps[length-1]
 
                # 이전 lps를 고려하지 않고, lps[i]를 계산
            else:
                lps[i] = 0
                i += 1


n = int(input())
m = int(input())
s = list(input().rstrip())
len_s = n * 2 + 1

n_s = ['I' if i % 2 == 0 else 'O' for i in range(len_s)]
# for i in range(m - len_s + 1):
#     if s[i:i+len_s] == n_s:
#         result += 1

# print(result)
