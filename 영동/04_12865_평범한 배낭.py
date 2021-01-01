# https://www.acmicpc.net/problem/12865

import sys
from collections import deque
combi = [[-1,[]] for i in range(100001)]

N,K = map(int,sys.stdin.readline().split())
objects = sorted(list(map(int, sys.stdin.readline().split())) for i in range(N))

queue = deque(objects)
tmp=deque([])

for i in range(len(objects)):
    combi[objects[i][0]][0] = objects[i][1] #value
    combi[objects[i][0]][1].append(objects[i][0]) #objects

while True:
    item = queue.popleft()
    for other in queue:


        breakflag=False
        #중복된 조합을 체크한다.
        overlap=[]
        for i in range(len(combi[item[0]][1])):  # 아이템 조합을 저장해놓는다.
            overlap.append(combi[item[0]][1][i])
        for i in range(len(combi[other[0]][1])):
            overlap.append(combi[other[0]][1][i])
        numvisit = [0 for i in range(101)] #중복된 숫자 체크
        for i in overlap:
            numvisit[i]+=1
        numcheck=[x for x in numvisit if x != 0] #0은 제거후 나머지만 반환
        for i in numcheck:
            if i != 1:
                breakflag=True
        if breakflag ==True: #
            continue




        if combi[item[0] + other[0]][0] == -1:#조합에 값이 없으면 조합 value를 넣는다
            combi[item[0] + other[0]][0] = item[1]+other[1] # values

            for i in range(len(combi[item[0]][1])): #아이템 조합을 저장해놓는다.
                combi[item[0] + other[0]][1].append(combi[item[0]][1][i])
            for i in range(len(combi[other[0]][1])):
                combi[item[0] + other[0]][1].append(combi[other[0]][1][i])

        else: #이미 들어있는 값이면 비교해야함.
            if item[1] + other[1]>combi[item[0] + other[0]][0]:# 기존에 있던 것이더 작으면
                combi[item[0] + other[0]][0] = item[1] + other[1] #value 값을 업데이트 하고
                combi[item[0] + other[0]][1]=[]#리스트를 교환한다.
                for i in range(len(combi[item[0]][1])):
                    combi[item[0] + other[0]][1].append(combi[item[0]][1][i])
                for i in range(len(combi[other[0]][1])):
                    combi[item[0] + other[0]][1].append(combi[other[0]][1][i])
        tmp.append([item[0]+other[0],item[1]+other[1]])

    for _ in range(len(tmp)):
        queue.append(tmp.popleft())

    # 종료 체크, 모든 아이템을 사용한 경우를 반환한다.
    endflag = False
    endcheck = [x for x in combi if x[0] != -1]
    for i in endcheck:
        if len(i[1]) == N:
            endflag = True
    if endflag == True:
        break

print(combi[K][0])