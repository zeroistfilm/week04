# https://www.acmicpc.net/problem/11047
def pro():
    import sys
    N, K = map(int, sys.stdin.readline().split())
    coins=[]

    for i in range(N):
        coin = int(sys.stdin.readline())
        if coin <=K:
            coins.append(coin)
    count=0
    tmp=K

    for coin in coins[::-1]:
        count+=K//coin
        K=K%coin
        if K==0:
            break
    print(count)
pro()