import sys
input = sys.stdin.readline


def bottomUp(n):
    global dp

    dp[0], dp[1] = (1,0), (0,1)
    for i in range(2, n+1):
        dp[i] = (dp[i-1][0] + dp[i-2][0], dp[i-1][1] + dp[i-2][1])

    return dp[n]


def topDown(n):
    global dp

    if n == 0:
        return (1,0)
    elif n == 1:
        return (0,1)
        
    if dp[n] != (0,0):
        return dp[n]
    
    tmp_ = topDown(n-1)
    tmp_2 = topDown(n-2)
    dp[n] = (tmp_[0] + tmp_2[0], tmp_[1] + tmp_2[1])

    return dp[n]


dp = [(0,0) for _ in range(41)]

if __name__ == "__main__":
    for _ in range(int(input())):
        print(' '.join(list(map(str, bottomUp(int(input()))))))