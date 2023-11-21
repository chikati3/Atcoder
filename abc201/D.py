H, W = map(int, input().split())
A = [input() for _ in range(H)]

INF = 10**10
dp = [[-INF] * W for _ in range(H)]
dp[H-1][W-1] = 0
for i in range(H-1, -1, -1):
    for j in range(W-1, -1, -1):

        if A[i][j] == '+':
            x = 1
        else:
            x = -1
        
        if 0 <= i - 1:
            dp[i-1][j] = max(dp[i-1][j], -dp[i][j] + x)
        if 0 <= j - 1:
            dp[i][j-1] = max(dp[i][j-1], -dp[i][j] + x)

if 0 < dp[0][0]:
    print('Takahashi')
elif dp[0][0] == 0:
    print('Draw')
else:
    print('Aoki')