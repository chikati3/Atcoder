n = int(input())
a = list(map(int, input().split()))
s = [input() for _ in range(n)]

INF = 10**18
dist = [[[INF, 0] for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(n):
        if s[i][j] == 'Y':
            dist[i][j][0] = 1
            dist[i][j][1] = a[j]

for k in range(n):
    for i in range(n):
        for j in range(n):
            d, c = dist[i][k][0] + dist[k][j][0], dist[i][k][1] + dist[k][j][1]
            if d < dist[i][j][0]:
                dist[i][j] = [d, c]
            elif dist[i][j][0] == d and dist[i][j][1] < c:
                dist[i][j][1] = c

q = int(input())
for _ in range(q):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    if dist[u][v][0] == INF:
        print('Impossible')
    else:
        print(dist[u][v][0], a[u] + dist[u][v][1])