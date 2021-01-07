# https://www.acmicpc.net/problem/2098
import sys

sys.stdin = open("input.txt", "r")
N = int(sys.stdin.readline())
W = []
INF = sys.maxsize
for _ in range(N):
    W.append(list(map(int, sys.stdin.readline().split())))
DP = [[None] * (1 << N) for _ in range(N)]


def find_path(last, visited):
    # 모든곳을 방문했을떄
    # DP에 값이 있을 떄

    # 그 외 나머지
    # 모든 도시를 돌면서, 방문하지 않았거나, 방문 비용이 0이 아닌곳을 방문한다.
    # 방문가능하다면, 최소 비용을 리턴한다.

    if visited == (1 << N) - 1:
        return W[last][0] or INF  # 0으로 돌아가는 비용 출력
    if DP[last][visited] is not None:
        return DP[last][visited]
    tmp = INF
    for city in range(N):
        if W[last][city] != 0 and visited & (1 << city) == 0:
            tmp = min(tmp, find_path(city, visited | 1 << city) + W[last][city])
    DP[last][visited] = tmp
    return tmp


print(find_path(0, 1 << 0))
