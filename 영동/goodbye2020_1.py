N = int(input())
words=list(map(str,input().split()))
check=False
visit=[0 for i in range(26)]
for i in range(len(words)):
    if words[i][-1]==words[i][0]:
        visit[ord(words[i][-1])-97]=1
        check=True
answer=[x for x in visit if x!=0]
if len(answer)==1:
    print(1)
else:
    print(0)