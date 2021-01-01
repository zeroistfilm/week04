# https://www.acmicpc.net/problem/1904

import sys
sys.setrecursionlimit(10**9)
tile={}
def solve(n):

    if n in tile:
        return n
    if n<=3:
        return n
    else:
        f = (solve(n-1)+solve(n-2))%15746
        tile[n]=f
        if len(tile) >= 3:
            del tile[n - 2]
        return f

print(solve(int(sys.stdin.readline())))