import sys
input = sys.stdin.readline

n, m = map(int, input().split())

pokemon = {}
for i, _ in enumerate(range(n), start=1):
    tmp = input().rstrip()
    pokemon[str(i)] = tmp
    pokemon[tmp] = i

for _ in range(m):
    tmp = input().rstrip()
    print(pokemon[tmp])