import sys
input = sys.stdin.readline

member = list()
for _ in range(int(input())):
    member.append(tuple(input().split()))
    
for m in sorted(member, key=lambda x: int(x[0])):
    print(m[0], m[1])