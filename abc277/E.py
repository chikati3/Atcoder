from collections import deque


n, m, k = map(int, input().split())

edge = [[] for _ in range(n*2)]
for _ in range(m):
    u, v, a = map(int, input().split())
    u -= 1
    v -= 1
    if a == 0:
        u += n
        v += n
    edge[u].append((v, 1))
    edge[v].append((u, 1))

s = list(map(int, input().split()))
for si in s:
    si -= 1
    u = si
    v = si + n
    edge[u].append((v, 0))
    edge[v].append((u, 0))

d = deque()
d.append(0)
INF = 10**20
dist = [INF] * (n*2)
dist[0] = 0
while d:
    x = d.popleft()
    for to, c in edge[x]:
        if dist[x] + c < dist[to]:
            dist[to] = dist[x] + c
            if c == 0:
                d.appendleft(to)
            else:
                d.append(to)
ans = min(dist[n-1], dist[n*2-1])
if ans == INF:
    print(-1)
else:
    print(ans)