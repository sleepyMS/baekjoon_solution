from collections import Counter

n = int(input())
n_num = Counter(list(input().split()))

m = int(input())
m_num = list(input().split())

result = " ".join([str(n_num[i]) for i in m_num])
print(result)