n = int(input())
a = list(map(int, input().split()))
mod = 998244353

# i個目までの中でj個選んだ時のmod_mがkの個数
def solve(m):
    dp = [[0]*(n+1) for _ in range(n+1)]
    dp[0][0] = 1
    for i in a:
        for j in range(n, 0, -1):
            for k in range(m):
                dp[j][k] += dp[j-1][(k - i) % m]
                dp[j][k] %= mod
    return dp[m][0]

ans = 0
for cnt in range(1, n+1):
    ans += solve(cnt)
    ans %= mod
print(ans)