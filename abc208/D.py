N, M = map(int, input().split())

INF = 10**10
dist = [[INF for _ in range(N)] for _ in range(N)]
for i in range(N):
    dist[i][i] = 0

for _ in range(M):
    A, B, C = map(int, input().split())
    A -= 1
    B -= 1
    dist[A][B] = C

ans = 0
for k in range(N):
    for i in range(N):
        for j in range(N):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
            if dist[i][j] != INF:
                ans += dist[i][j]
print(ans)