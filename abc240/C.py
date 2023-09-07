n, x = map(int, input().split())

dp = [[False]*(x+1) for _ in range(n+1)]
dp[0][0] = True
for i in range(n):
    a, b = map(int, input().split())
    for j in range(x+1):
        if dp[i][j] == True:
            if j+a <= x:
                dp[i+1][j+a] = dp[i][j]
            if j+b <= x:
                dp[i+1][j+b] = dp[i][j]
if dp[n][x] == True:
    print('Yes')
else:
    print('No')