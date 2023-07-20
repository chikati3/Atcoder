n, p = map(int, input().split())
mod = 998244353

# 逆元
p = p * pow(100, mod-2, mod) % mod
dp = [0] * (n+1)
for i in range(1, n+1):
    dp[i] = (1 + dp[i-2] * p + dp[i-1] * (1-p))
    dp[i] %= mod
print(dp[n])