n = int(input())
n_arr = set(map(int, input().split()))
m = int(input())
m_arr = list(map(int, input().split()))

for i in m_arr:
    print(1) if i in n_arr else print(0)