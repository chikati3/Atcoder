N, W = map(int, input().split())

dp = [-1] * (W+1)
dp[0] = 0

for i in range(1, N+1):
    w, v = map(int, input().split())
    for j in range(W, -1, -1):
        if 0 <= dp[j] and j + w <= W:
            dp[j+w] = max(dp[j+w], dp[j] + v)
print(max(dp[1:]))