N, M, K = map(int, input().split())
mod = 998244353

uv = []
for _ in range(M):
    u, v = map(int, input().split())
    uv.append((u, v))

dp = [[0]*(N+1) for _ in range(K+1)]
dp[0][1] = 1
for i in range(K):
    s = sum(dp[i])
    for j in range(1, N+1):
        dp[i+1][j] = s - dp[i][j]
    for u, v in uv:
        dp[i+1][u] -= dp[i][v]
        dp[i+1][v] -= dp[i][u]
    for j in range(1, N+1):
        dp[i+1][j] %= mod
print(dp[K][1])