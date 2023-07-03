# ゲームは後ろから計算

n, a, b, p, q = map(int, input().split())

mod = 998244353
ip = pow(p, mod-2, mod)
iq = pow(q, mod-2, mod)
dp = [[[0, 0] for _ in range(n+1)] for _ in range(n+1)]

# ゴールから調べる
for i in range(n, a-1, -1):
    for j in range(n, b-1, -1):
        if i == n:
            # 勝ち
            dp[i][j] = [1, 1]
        elif j == n:
            # 負け
            dp[i][j] = [0, 0]
        else:
            # 行き先の平均
            for k in range(1, p+1):
                dp[i][j][0] += dp[min(i+k, n)][j][1]
            dp[i][j][0] = dp[i][j][0] * ip % mod
            for k in range(1, q+1):
                dp[i][j][1] += dp[i][min(j+k, n)][0]
            dp[i][j][1] = dp[i][j][1] * iq % mod
print(dp[a][b][0])