import sys
input = sys.stdin.readline

n, m = map(int, input().split())
tree = list(map(int, input().split()))
max_tree, min_tree = max(tree), 1
result = 0

while min_tree <= max_tree:
    tmp, mid_tree = 0, (min_tree + max_tree) // 2
    for i in tree:
        if mid_tree < i:
            tmp += i - mid_tree

    if m == tmp:
        result = mid_tree
        break
    elif m <= tmp:
        result = mid_tree
        min_tree = mid_tree + 1
    else:
        max_tree = mid_tree - 1
    
print(result)