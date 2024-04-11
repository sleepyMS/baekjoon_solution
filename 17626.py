n = int(input())
squares = set([i**2 for i in range(1, int(n**0.5)+1)])
result = 4

for i in range(1, int(n**0.5) + 1): 
    for j in range(1, int((n - i**2)**0.5) + 1):
        if (n - i*i - j*j) in squares:
            result = 3
            
for i in range(1, int(n**0.5) + 1):
    if (n-i**2) in squares:
        result = 2
        
if n in squares or n == 1:
    result = 1

print(result)
