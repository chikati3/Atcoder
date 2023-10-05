N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

mod = 998244353

dp = [[0] * (max(B) + 1) for _ in range(N+1)]
dp[0][0] = 1
for i in range(N):
    a = A[i]
    b = B[i]
    x = sum(dp[i][:a]) % mod
    for c in range(a, b+1):
        x = (x + dp[i][c]) % mod
        dp[i+1][c] += x
        dp[i+1][c] %= mod
print(sum(dp[N]) % mod)