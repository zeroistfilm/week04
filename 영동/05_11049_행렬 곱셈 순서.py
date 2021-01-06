# https://www.acmicpc.net/problem/11049

import sys

#sys.stdin = open("input.txt", "r")

N = int(sys.stdin.readline())
M = [0 for i in range(N+1)]
for i in range(N):
    a,b = map(int, sys.stdin.readline().split())
    M[i]=a
    M[i+1] = b
Matrix = [[0 for i in range(N)] for i in range(N)]

for i in range(1,N):
    r = 0
    c = i
    for _ in range(N,i,-1):
        tmp=[]
        for k in range(r,c):
            tmp.append(Matrix[r][k]+Matrix[k+1][c]+(M[r]*M[k+1]*M[c+1]))
        Matrix[r][c]=min(tmp)
        r += 1
        c += 1

print(Matrix[0][-1])
