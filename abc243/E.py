n, m = map(int, input().split())

INF = 10**12
dist = [[INF]*n for _ in range(n)]
abc = []
for i in range(n):
    dist[i][i] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    dist[a][b] = c
    dist[b][a] = c
    abc.append([a, b, c])

for k in range(n):
    for i in range(n):
        for j in range(n):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

ans = 0
for a, b, c in abc:
    for k in range(n):
        if a == k or b == k:
            continue
        if dist[a][k] + dist[k][b] <= c:
            ans += 1
            break
print(ans)