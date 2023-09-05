n = int(input())
mod = 998244353

dp = [[0]*10 for _ in range(n)]
dp[0] = [1]*10
for i in range(n-1):
    for j in range(1, 10):
        dp[i+1][j] += dp[i][j]
        dp[i+1][j] %= mod
        if j < 9:
            dp[i+1][j+1] += dp[i][j]
            dp[i+1][j+1] %= mod
        if 1 < j:
            dp[i+1][j-1] += dp[i][j]
            dp[i+1][j-1] %= mod
print(sum(dp[n-1]) % mod)