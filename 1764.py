import sys
input = sys.stdin.readline

n, m = map(int, input().split())
n_set = {input().rstrip() for _ in range(n)}
m_set = {input().rstrip() for _ in range(m)}
result = [s for s in n_set if s in m_set]

print(len(result))
result.sort()
for r in result:
    print(r)