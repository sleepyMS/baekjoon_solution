from itertools import product

n = int(input())
m = int(input())
con = []
if m:
    con = list(input().split())
defaultCon = [str(i) for i in range(10)]

remove = []
for i in defaultCon:
    if i in con:
        remove.append(i)

for i in remove:
    defaultCon.remove(i)

channel = [100]
for cwr in product(defaultCon, repeat=len(str(n))):
    if len(cwr) != 1 and cwr[0] == '0':
        continue
    channel.append(int(''.join(cwr)))

for cwr in product(defaultCon, repeat=len(str(n)) + 1):
    if cwr[0] == '0':
        continue
    channel.append(int(''.join(cwr)))
    break

for cwr in product(sorted(defaultCon, reverse=True), repeat=len(str(n)) - 1):
    if len(cwr) == 0:
        break
    if len(cwr) != 1 and cwr[0] == '0':
        continue
    channel.append(int(''.join(cwr)))
    break

result = []
for i in channel:
    if i == 100:
        result.append(abs(n - i))
    else:
        result.append(abs(n - i) + len(str(i)))

print(min(result))