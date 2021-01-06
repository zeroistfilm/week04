# https://www.acmicpc.net/problem/1700

import sys
N, K = map(int, sys.stdin.readline().split())
items=list(map(int,sys.stdin.readline().strip().split()))
soket=[0 for i in range(N)]


answer=0
for i in range(K):
    cable = items[i]
    #소켓이 비어있는가
    #빈곳이 없는가
    #기기가 꽂혀있는

    for k in range(len(soket)):
        soketindex = -1
        if soket[k]==0:
            soketindex=k
            break
    breakflag = False
    if cable in soket: #기기가 꽂혀있는지

        continue

    elif soketindex!=-1: #소켓이 비어있음
        soket[soketindex]=cable
        continue

    else: #빈 포트가 없으면 현재 꽂혀 있는 아이템 중에 나중에 가장 늦게 사용하는 아이템 포트를 뺸다.
        answer+=1
        check = [0 for i in range(len(soket))]
        for j in range(len(soket)):
            if not soket[j] in items[i:]: #앞으로도 안쓰면 뽑는다.
                soket[j] = cable
                breakflag=True
                break
            else:
                #나중에 쓰일 순서
                check[j]=items[i:].index(soket[j])
        if breakflag==True:
            continue
        soket[check.index(max(check))]=cable#교체해도 되는 인덱스임

print(answer)