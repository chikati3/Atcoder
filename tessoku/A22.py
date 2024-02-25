N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A = [A[i] - 1 for i in range(N-1)]
B = [B[i] - 1 for i in range(N-1)]

dp = [-10**10] * N
dp[0] = 0
for i in range(N-1):
    dp[A[i]] = max(dp[A[i]], dp[i] + 100)
    dp[B[i]] = max(dp[B[i]], dp[i] + 150)
print(dp[N-1])