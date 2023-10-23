from collections import deque


N, M = map(int, input().split())
mod = 10**9+7

edge = [[]for _ in range(N)]
for _ in range(M):
    A, B = map(int, input().split())
    A -= 1
    B -= 1
    edge[A].append(B)
    edge[B].append(A)

d = deque()
d.append(0)
dist = [-1] * N
dist[0] = 0
cnt = [0] * N
cnt[0] = 1
while d:
    x = d.popleft()
    for to in edge[x]:
        if dist[to] == -1:
            dist[to] = dist[x] + 1
            d.append(to)
            cnt[to] += cnt[x]
            cnt[to] %= mod
        elif dist[to] == dist[x] + 1:
            cnt[to] += cnt[x]
            cnt[to] %= mod
print(cnt[N-1])