n, m, k = map(int, input().split())
abc = [list(map(int, input().split())) for _ in range(m)]
e = list(map(int, input().split()))

INF = 10**20
dist = [INF] * n
dist[0] = 0
for i in range(k):
    a, b, c = abc[e[i] - 1]
    a -= 1
    b -= 1
    dist[b] = min(dist[b], dist[a] + c)

if dist[n-1] == INF:
    print(-1)
else:
    print(dist[n-1])