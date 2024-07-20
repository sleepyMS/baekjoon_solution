from itertools import permutations

n, m = map(int, input().split())
arr = map(int, input().split())

per = sorted(list(permutations(arr, m)))
for i in per:
    tmp = map(str, i)
    print(' '.join(tmp))

