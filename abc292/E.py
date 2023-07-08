from collections import deque


n, m = map(int, input().split())

edge = [[] for _ in range(n)]
for _ in range(m):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    edge[u].append(v)

cnt = 0
for i in range(n):
    d = deque()
    d.append(i)
    dist = [False] * n
    dist[i] = True
    while d:
        x = d.popleft()
        for to in edge[x]:
            if dist[to] != False:
                continue
            dist[to] = True
            d.append(to)
            cnt += 1
print(cnt - m)