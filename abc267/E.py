from heapq import heappop, heappush


n, m = map(int, input().split())
a = list(map(int, input().split()))

cost = [0] * n
edge = [[] for _ in range(n)]
for _ in range(m):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    edge[u].append(v)
    edge[v].append(u)
    cost[u] += a[v]
    cost[v] += a[u]

hq = []
for i in range(n):
    heappush(hq, (cost[i], i))

seen = set()
INF = 10**20
ans = -INF
while hq:
    c, x = heappop(hq)
    if x in seen or cost[x] < c:
        continue
    seen.add(x)
    ans = max(ans, c)
    for to in edge[x]:
        cost[to] -= a[x]
        heappush(hq, (cost[to], to))
print(ans)