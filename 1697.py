import queue

def BFS(filed, n, k):
    que = queue.deque([n])

    while que:
        tmp = que.popleft()

        for i in (tmp-1, tmp+1, tmp*2):
            if 0 <= i <= 100000 and filed[i] == 0:
                filed[i] = filed[tmp] + 1
                if i == k:
                    return filed[i]
                que.append(i)


if __name__ == "__main__":
    n, k = map(int, input().split())
    filed = [0] * 100001

    if n == k:
        print(0)
    else:
        print(BFS(filed, n, k))