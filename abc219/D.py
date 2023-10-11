N = int(input())
X, Y = map(int, input().split())

INF = 10**18
dp = [[INF]*(Y+1) for _ in range(X+1)]
dp[0][0] = 0

for _ in range(N):
    a, b = map(int, input().split())
    for i in range(X, -1, -1):
        for j in range(Y, -1, -1):
            xi = min(X, i+a)
            yi = min(Y, j+b)
            dp[xi][yi] = min(dp[xi][yi], dp[i][j] + 1)
if dp[-1][-1] <= N:
    print(dp[-1][-1])
else:
    print(-1)