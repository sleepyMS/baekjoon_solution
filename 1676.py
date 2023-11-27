n = int(input())

count = 0
while n / 5 >= 1:
    count += n // 5
    n //= 5
    
print(count)