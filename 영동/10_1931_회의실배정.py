# https://www.acmicpc.net/problem/1931

import sys
N = int(sys.stdin.readline())
meetings =[]

for i in range(N):
    start, end = map(int, sys.stdin.readline().split())
    tmp = [start,end]
    meetings.append(tmp)
meetings.sort(key=lambda x:(x[0]))
meetings.sort(key=lambda x:(x[1]))
meeting_count=0
start_time=0
for time in meetings:
    if time[0]>= start_time:
        start_time=time[1]
        meeting_count+=1

print(meeting_count)