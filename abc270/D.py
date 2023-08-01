n, k = map(int, input().split())
a = list(map(int, input().split()))

dp = [0] * (n+1)
for i in range(1, n+1):
    for ai in a:
        if i - ai < 0:
            break
        dp[i] = max(dp[i], i - dp[i - ai])
print(dp[n])