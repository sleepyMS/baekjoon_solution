import sys
input = sys.stdin.readline


if __name__ == "__main__":
    n = int(input().strip())
    x = list(map(int, input().split()))
    sorted_x = sorted(list(set(x)))
    tmp = {a: i for i, a in enumerate(sorted_x)}

    for i in x:
        print(tmp[i], end =' ')

        