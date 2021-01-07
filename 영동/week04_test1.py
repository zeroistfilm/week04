# https://www.acmicpc.net/problem/2579

import sys
sys.stdin = open("input.txt", "r")

N = int(sys.stdin.readline())
stairs=[]
for i in range(N):
    stairs.append(int(sys.stdin.readline()))
dp = [[-1 for i in range(N+1)]for i in range(5)]
dp[0][0]=0
for i in range(N + 1):
    for k in range(3):
        if dp[k][i]!=-1:
            #여기 들어오는 v,i를 기준으로 새로운 2가지 길 제시
            for v in [1, 2]:

                if i != 0 and dp[v][i+v-1] != -1 and dp[v][i+v-2] != -1:
                    continue

                dp[v][i+v] = max(dp[v][i+v] ,dp[k][i] + stairs[i+v-1]) #1칸 가거나 2칸 가거나해서 해당하는 계단의 값을 dp에 저장한다

print('a')