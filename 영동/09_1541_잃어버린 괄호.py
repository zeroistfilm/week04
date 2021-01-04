# https://www.acmicpc.net/problem/1541

import sys

expression = list(sys.stdin.readline().strip().split('-'))
result=[]
# 05+01-10

for tmp in expression:
    if '+' in tmp:
        tmp2 = []
        for i in tmp.split('+'):
            tmp2.append(int(i))
        result.append(sum(tmp2))
    else:
        result.append(int(tmp))

answer = result[0]
for i in range(1,len(result)):
    answer-=result[i]
print(answer)