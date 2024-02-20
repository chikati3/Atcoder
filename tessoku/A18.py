N, S = map(int, input().split())
A = list(map(int, input().split()))

dp = [False] * (S+1)
dp[0] = True
for i in range(N):
    for j in range(S, -1, -1):
        if dp[j] == True and j + A[i] <= S:
            dp[j + A[i]] = True
if dp[S] == True:
    print('Yes')
else:
    print('No')