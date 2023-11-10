N = int(input())
A = list(map(int, input().split()))

ma = sum(A)

dp = [[False] * (ma+1) for _ in range(N+1)]
dp[0][0] = True

for i in range(N):
    for j in range(ma+1):
        if A[i] + j <= ma:
            dp[i+1][A[i]+j] = dp[i][j]
        dp[i+1][j] = dp[i+1][j] | dp[i][j]

ans = float('inf')
for i in range(ma):
    if dp[N][i]:
        ans = min(ans, max(i, ma-i))
print(ans)