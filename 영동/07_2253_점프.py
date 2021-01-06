# https://www.acmicpc.net/problem/2253
import sys

INF =9999
sys.stdin = open("input.txt", "r")
N,M = map(int, sys.stdin.readline().split())
stone = []
for i in range(M):
    index =int(sys.stdin.readline())
    stone.append(index)
DP=[[0 for i in range(N+1)]for i in range(int((N**0.5))+N)]
#dp인덱스 나중에 수정하기
for i in range(len(DP)):
    DP[i][-1]= INF

recursive = 0
def jump(node,velo,count):
    global recursive
    recursive+=1
    if node > N:
        return
    if node in stone:  # 트랩임.
        return

    if DP[velo][node] == 0 or DP[velo][node] == INF:
        DP[velo][node] = count
    else:
        return

    if node==1:
        DP[velo][node] = 's'
        node+=velo
        jump(node,velo,count+1)
    for v in [velo+1,velo, velo-1]:
        if v<=0:
            continue
        else:
            if node > N:
                return

            jump(node+v, v, count + 1)

jump(node=1,velo=1,count=0)
#print(recursive)
result =min(DP[i][-1] for i in range(len(DP)))
if result ==INF:
    print(-1)
else:
    print(result)