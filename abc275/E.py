n, m, k = map(int, input().split())

mod = 998244353
inv = pow(m, mod-2, mod)

dp = [[0]*(n+1) for _ in range(k+1)]
dp[0][0] = 1
for i in range(k):
    for j in range(n):
        for v in range(1, m+1):
            if j+v <= n:
                dp[i+1][j+v] += dp[i][j] * inv
                dp[i+1][j+v] %= mod
            else:
                over = j+v - n
                dp[i+1][n - over] += dp[i][j] * inv
                dp[i+1][n - over] %= mod
ans = 0
for i in range(k+1):
    ans += dp[i][n]
    ans %= mod
print(ans)