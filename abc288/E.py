n, m = map(int,input().split())
a = list(map(int,input().split()))
c = list(map(int,input().split()))
x = set(list(map(int,input().split())))

INF = float('inf')
dp = [[INF]*(n+1) for _ in range(n+1)]
dp[0][0] = 0

for i in range(n):
    # 買う順番のコスト
    mi = [INF]*(n+1)
    for j in range(i,-1,-1):
        mi[j] = min(mi[j+1], c[j])

    for j in range(i+1):
        if not i+1 in x:
            # 買わない
            dp[i+1][j] = min(dp[i+1][j], dp[i][j])
        # 買う
        dp[i+1][j+1] = min(dp[i+1][j+1], dp[i][j] + a[i] + mi[i-j])
print(min(dp[-1]))