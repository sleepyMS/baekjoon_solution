# n = int(input())
# tanghulu = list(input().split())
# len_tanghulu = len(tanghulu)
# result = 0

# for i in range(len_tanghulu//2 + 1):
#     for j in range(i+2, len_tanghulu-i+1):
#         tmp = tanghulu[i:j]
#         tmp2 = tanghulu[len_tanghulu-j+1:len_tanghulu-i]
#         len_tmp, len_tmp2 = len(tmp), len(tmp2)
#         len_set_tmp, len_set_tmp2 = len(set(tmp)), len(set(tmp2))
#         if len_set_tmp <= 2 or len_set_tmp2 <= 2:
#             if len_set_tmp <= 2 and len_tmp > result:
#                 result = len_tmp
#             if len_set_tmp2 <= 2 and len_tmp2 > result:
#                 result = len_tmp2
#         else:
#             break
        
# print(result) 교1팀 오윤경 선생님 부재중


n = int(input())
tanghulu = input().split()
count = {}
left = 0
result = 0

for right in range(n):
    if tanghulu[right] in count:
        count[tanghulu[right]] += 1
    else:
        count[tanghulu[right]] = 1
    
    while len(count) > 2:
        count[tanghulu[left]] -= 1
        if count[tanghulu[left]] == 0:
            del count[tanghulu[left]]
        left += 1
    
    result = max(result, right - left + 1)
    
print(result)