n, k, d = map(int, input().split())
a = list(map(int, input().split()))

dp = [[-1] * d for _ in range(k+1)]
dp[0][0] = 0

for ai in a:
    for j in range(k-1, -1, -1):
        for v in range(d):
            if dp[j][v] != -1:
                dp[j+1][(v+ai)% d] = max(dp[j+1][(v+ai)%d], dp[j][v] + ai)
print(dp[k][0])