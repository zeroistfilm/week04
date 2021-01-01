# https://www.acmicpc.net/problem/1904

import sys
from collections import deque
n = int(sys.stdin.readline())
if n<3:
    print(n)
    exit()
queue=deque([])
queue.append(1)
queue.append(2)
for i in range(n-2):
    n1 = queue.popleft()
    n2 = queue[0]
    n3 = (n1+n2)%15746
    queue.append(n3)
print(queue.pop())
