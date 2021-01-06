# https://www.acmicpc.net/problem/12865

import sys
N, K  = map(int, sys.stdin.readline().split())
items = [list(map(int, sys.stdin.readline().split())) for i in range(N)]
dp = [[0 for i in range(K+1)]for i in range(len(items)+1)]


def sovle():
    for c in range(K+1):
        for r in range(1,len(items)+1):
            limitW = c
            weight = items[r-1][0]
            value = items[r-1][1]
            if weight > limitW:
                dp[r][c] = dp[r-1][c]
            else:
                dp[r][c] = max(dp[r-1][c], dp[r-1][c-weight]+value)
    print(dp[-1][-1])
sovle()