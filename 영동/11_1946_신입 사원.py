# https://www.acmicpc.net/problem/1946
import sys

N = int(sys.stdin.readline())
def pro():
    applys = [[] for _ in range(N)]
    for i in range(N):
        M = int(sys.stdin.readline())
        for j in range(M):
            apply = list(map(int, sys.stdin.readline().split()))
            applys[i].append([apply[0], apply[1]])

    for i in range(len(applys)):
        applys[i].sort(key=lambda x: x[0])
        count=1
        limit = applys[i][0][1]
        for j in range(1, len(applys[i])):
            if applys[i][j][1]<=limit:
                count+=1
                limit = applys[i][j][1]

        print(count)

pro()

