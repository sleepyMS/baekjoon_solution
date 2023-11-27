a, b = map(int, input().split())
c = int(input())

a += (b + c) // 60
b = (b + c) % 60

print(a%24, b)