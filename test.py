pattern = 'ABAABAB'

# KMP를 위한 table 만들기
pattern_table = [0] * (len(pattern))
j = 0
for i in range(1,len(pattern_table)):
    while j > 0 and pattern[i] != pattern[j]:
        j = pattern_table[j-1]
    if pattern[i] == pattern[j]:
        j += 1
        pattern_table[i] = j
    
print(pattern_table)
