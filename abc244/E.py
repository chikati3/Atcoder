n, m, k, s, t, x = map(int, input().split())
mod = 998244353

edge = [[] for _ in range(n+1)]
for _ in range(m):
    u, v = map(int, input().split())
    edge[u].append(v)
    edge[v].append(u)

dp = [[[0, 0] for _ in range(n+1)] for _ in range(k+1)]
dp[0][s][0] = 1
for i in range(k):
    for j in range(1, n+1):
        for e in edge[j]:
            if e == x:
                dp[i+1][e][0] += dp[i][j][1]
                dp[i+1][e][1] += dp[i][j][0]
            else:
                dp[i+1][e][0] += dp[i][j][0]
                dp[i+1][e][1] += dp[i][j][1]
            dp[i+1][e][0] %= mod
            dp[i+1][e][1] %= mod
print(dp[k][t][0])