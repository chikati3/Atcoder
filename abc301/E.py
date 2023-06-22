
# BFS & 巡回セールスマン問題(bitDP)
# bfsで頂点同志の距離を求める
# bitDPで指定頂点の最短距離を求める

from collections import deque


H, W, T = map(int, input().split())
B = [input() for _ in range(H)]

p, s, g = [], (-1, -1), (-1, -1)
for i in range(H):
    for j in range(W):
        if B[i][j] == 'o':
            p.append((i, j))
        elif B[i][j] == 'S':
            s = i, j
        elif B[i][j] == 'G':
            g = i, j
p.append(g)
p.append(s)
N = len(p)
INF = float('inf')

def bfs(sy, sx):
    d = [[INF for _ in range(W)] for _ in range(H)]
    d[sy][sx] = 0
    q = deque([(sy, sx)])
    while len(q):
        y, x = q.popleft()
        for dy, dx in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            y2, x2 = y + dy, x + dx
            if 0 <= y2 < H and 0 <= x2 < W and B[y2][x2] != '#' and d[y2][x2] == INF:
                d[y2][x2] = d[y][x] + 1
                q.append((y2, x2))
    return [d[y][x] for y, x in p]

# o, s, g頂点距離
d = [bfs(*q) for q in p]

# DP[通った頂点][現在の頂点]
dp = [[INF for _ in range(N)] for _ in range(1 << (N - 1))]
dp[0][N - 1] = 0
for bit in range(1 << (N - 1)):
    for now in range(N):
        for nxt in range(N - 1):
            dp[bit | 1 << nxt][nxt] = min(dp[bit | 1 << nxt][nxt], dp[bit][now] + d[now][nxt])

ans = -1
# Gに辿り着く歩数(T)
for bit in range(1 << (N - 1)):
    if dp[bit][N - 2] <= T:
        ans = max(ans, bin(bit).count('1') - 1)
print(ans)