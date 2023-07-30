n, s = map(int, input().split())

dp = [[False]*(s+1) for _ in range(n+1)]
dp[0][0] = True

x = []
for i in range(n):
    a, b = map(int, input().split())
    for j in range(s+1):
        if j+a <= s:
            dp[i+1][j+a] |= dp[i][j]
        if j+b <= s:
            dp[i+1][j+b] |= dp[i][j]
    x.append([a, b])

now = s
if dp[n][s] == True:
    ans = ''
    for i in range(n-1, -1, -1):
        a, b = x[i]
        if 1 <= dp[i][now - a] == True:
            ans += 'H'
            now -= a
        elif 1 <= dp[i][now - b] == True:
            ans += 'T'
            now -= b
    print('Yes')
    print(ans[::-1])
else:
    print('No')
