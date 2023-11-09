N = int(input())
A = list(map(int, input().split()))

dp = [[0] * (sum(A) + 1) for _ in range(N+1)]
dp[0][0] = 1

for i in range(N):
    for j in range(sum(A)+1):
        if 0 <= j - A[i]:
            dp[i+1][j] = dp[i][j] or dp[i][j - A[i]]
        else:
            dp[i+1][j] = dp[i][j]

ans = float('inf')
for i in range(sum(A)):
    if dp[N][i]:
        ans = min(ans, max(i, sum(A)-i))
print(ans)