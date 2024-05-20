import sys
input = sys.stdin.readline


def DFS(net, start=1):
    stack = [start]
    result = set()

    while stack:
        tmp = stack.pop()
        if tmp in net:
            for i in net[tmp]:
                if i not in result and i != 1:
                    stack.append(i)
                    result.add(i)

    return len(result)

if __name__ == "__main__":
    n = int(input())
    net = {}
    for _ in range(int(input())):
        a, b = map(int, input().split())
         
        if a in net:
            net[a].add(b)
        else:
            net[a] = set([b])
        if b in net:
            net[b].add(a)
        else:
            net[b] = set([a])

    print(DFS(net))

