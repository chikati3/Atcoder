
n, m = map(int, input().split())
mod = 998244353

# i番目の同じ値、i番目の異なる値
dp = [[0, 0] for _ in range(n+1)]
dp[1][0] = m % mod

# 同じ場合は一つ前と異なる必要がある
# 異なる場合は、もう一つ前と異なる必要がある
for i in range(2, n+1):
    dp[i][0] = dp[i - 1][1]
    dp[i][1] = dp[i - 1][0] * (m - 1) + dp[i - 1][1] * (m - 2)
    dp[i][0] %= mod
    dp[i][1] %= mod
print(dp[n][1])