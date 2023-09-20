H, W = map(int, input().split())
c = [input() for _ in range(H)]

dist = [[-1]*W for _ in range(H)]
dist[0][0] = 1
for i in range(H):
    for j in range(W):
        if c[i][j] == '#':
            continue
        if 0 <= i-1 and dist[i-1][j] != -1:
            dist[i][j] = dist[i-1][j] + 1
        if 0 <= j-1 and dist[i][j-1] != -1:
            dist[i][j] = dist[i][j-1] + 1
ans = 0
for d in dist:
    ans = max(ans, max(d))
print(ans)