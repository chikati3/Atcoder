from collections import deque


n, m = map(int, input().split())

edge = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    edge[a].append(b)
    edge[b].append(a)

q = int(input())
for _ in range(q):
    x, k = map(int, input().split())
    ans = 0

    d = deque()
    d.append(x)
    dist = {}
    dist.setdefault(x, 0)
    while d:
        v = d.popleft()
        ans += v
        if dist[v] == k:
            continue
        for to in edge[v]:
            if to in dist:
                continue
            dist.setdefault(to, dist[v] + 1)
            d.append(to)
    print(ans)