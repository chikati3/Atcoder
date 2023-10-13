from collections import deque
from heapq import heappop, heappush


Q = int(input())

d = deque()
pq = []
for _ in range(Q):
    que = list(map(int, input().split()))
    if que[0] == 1:
        d.append(que[1])
    elif que[0] == 2:
        if len(pq) <= 0:
            print(d.popleft())
        else:
            print(heappop(pq))
    elif que[0] == 3:
        while d:
            heappush(pq, d.popleft())