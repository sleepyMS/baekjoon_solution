n = int(input())
size = map(int, input().split())
t, p = map(int, input().split())

print(sum([i//t+1 if i%t else i//t for i in size]))
print(' '.join(map(str, [n//p, n%p])))

