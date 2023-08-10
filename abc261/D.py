n, m = map(int, input().split())
x = list(map(int, input().split()))

cy = [0] * (n+1)
for _ in range(m):
    c, y = map(int, input().split())
    c -= 1
    cy[c] = y

INF = 10**18
dp = [[-INF]*(n+1) for _ in range(n+1)]
dp[0][0] = 0
for i in range(n):
    for j in range(n):
        dp[i+1][0] = max(dp[i+1][0], dp[i][j])
        dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j] + x[i] + cy[j])

print(max(dp[n]))