from collections import deque


N, Q = map(int, input().split())

edge = [[] for _ in range(N)]
for _ in range(N-1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    edge[a].append(b)
    edge[b].append(a)

deq = deque()
deq.append(0)
dist = [-1] * N
dist[0] = 0
while deq:
    x = deq.popleft()
    for to in edge[x]:
        if dist[to] != -1:
            continue
        dist[to] = dist[x] + 1
        deq.append(to)

for _ in range(Q):
    c, d = map(int, input().split())
    c -= 1
    d -= 1
    diff = abs(dist[c] - dist[d])
    if diff % 2 == 0:
        print('Town')
    else:
        print('Road')