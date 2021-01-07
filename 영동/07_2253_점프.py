import sys
from math import sqrt
input = sys.stdin.readline


def solve():
    N, M = map(int, input().split())

    dp = [[float('inf')]*(int(1.5*(N**0.5) + 2)) for _ in range(N+1)]
    dp[1][0] = 0
    trap = set()
    for _ in range(M):
        trap.add(int(input()))

    for i in range(2, N+1):
        if i in trap:
            continue
        for v in range(1, int(sqrt(2*i))+1):
            dp[i][v] = min(dp[i-v][v-1], dp[i-v][v], dp[i-v][v+1]) + 1

    result = min(dp[N])
    if result == float('inf'):
        print(-1)
    else:
        print(result)


solve()