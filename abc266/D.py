n = int(input())

num = 10**5

t = [[0, 0] for _ in range(num+1)]
for _ in range(n):
    ti, x, a = map(int, input().split())
    t[ti] = [x, a]   

dp = [[0]*5 for _ in range(num+1)]
for i in range(1, num+1):
    dp[i][0] = max(dp[i-1][0], dp[i-1][1])
    dp[i][1] = max(dp[i-1][0], dp[i-1][1], dp[i-1][2])
    dp[i][2] = max(dp[i-1][1], dp[i-1][2], dp[i-1][3])
    dp[i][3] = max(dp[i-1][2], dp[i-1][3], dp[i-1][4])
    dp[i][4] = max(dp[i-1][3], dp[i-1][4])

    x, a = t[i]
    if x <= i:
        dp[i][x] += a
print(max(dp[num]))