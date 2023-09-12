from heapq import heappop, heappush


N, M = map(int, input().split())
H = list(map(int, input().split()))

edge = [[] for _ in range(N)]
for _ in range(M):
    U, V = map(int, input().split())
    U -= 1
    V -= 1
    if H[V] >= H[U]:
        U, V = V, U
    diff = H[U] - H[V]
    edge[U].append((V, 0))
    edge[V].append((U, diff))

def dijkstra(s):
    pq = []
    dist = [10**18] * N
    dist[s] = 0
    heappush(pq, (0, s))

    while pq:
        d, frm = heappop(pq)
        if dist[frm] < d:
            continue
        for to, cost in edge[frm]:
            if dist[to] > dist[frm] + cost:
                dist[to] = dist[frm] + cost
                heappush(pq, (dist[to], to))
    return dist

dist = dijkstra(0)
ans = 0
for i in range(N):
    ans = max(ans, -(H[i] + dist[i] - H[0]))
print(ans)