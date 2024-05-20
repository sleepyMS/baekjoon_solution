import sys
input = sys.stdin.readline

# print(max([i*a for i, a in enumerate(sorted([int(input()) for _ in range(int(input()))], reverse=True), start=1)]))


n = int(input())
rope = [int(input()) for _ in range(n)]

downRope = sorted(rope, reverse=True)

result = []
for i, r in enumerate(downRope, start=1):
    result.append(i * r)

print(max(result))


