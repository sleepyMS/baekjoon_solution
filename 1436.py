n = int(input())

i, count = 0, 0
while True:
    i += 1
    if '666' in str(i):
        count += 1

    if count == n:
        print(i)
        break