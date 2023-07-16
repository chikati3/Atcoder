n, x = map(int, input().split())

dp = [False] * (x+1)
dp[0] = True

for _ in range(n):
    a, b = map(int, input().split())
    for i in range(x-1, -1, -1):
        if dp[i] == True:
            for j in range(1, b+1):
                if i+a*j <= x:
                    dp[i+a*j] = True
if dp[x] == True:
    print('Yes')
else:
    print('No')