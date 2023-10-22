S = input()
n = len(S)

mod = 10**9+7

x = '_chokudai'
dp = [0] * len(x)
dp[0] = 1
for i in range(n):
    for j in range(len(x)):
        if S[i] == x[j]:
            dp[j] += dp[j-1]
            dp[j] %= mod
print(dp[-1] % mod)