# https://www.acmicpc.net/problem/9251
import sys
word1 = str(sys.stdin.readline().strip())
word2 = str(sys.stdin.readline().strip())

M = [[0 for i in range(len(word1)+1)] for i in range(len(word2)+1)]

for r in range(1,len(word2)+1):
    for c in range(1,len(word1)+1):
        if word1[c-1]==word2[r-1]:
            M[r][c]=M[r-1][c-1]+1
        else:
            M[r][c] = max(M[r-1][c],M[r][c-1])

print(M[-1][-1]) #row/cols

