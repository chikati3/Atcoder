N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

memo = [[False, False] for _ in range(N)]
memo[0] = [True, True]
memo[1][0] = True

INF = float('inf')
dp = [INF] * N
dp[0] = 0
dp[1] = A[0]
for i in range(2, N):
    a = dp[i-1] + A[i-1]
    b = dp[i-2] + B[i-2]

    dp[i] = min(dp[i], a)
    dp[i] = min(dp[i], b)
    if a == b:
        memo[i] = [True, True]
    elif a < b:
        memo[i][0] = True
    elif a > b:
        memo[i][1] = True

ans = [N]
x = N
while 1 < x:
    if memo[x-1][0] == True:
        x -= 1
        ans.append(x)
    elif memo[x-1][1] == True:
        x -= 2
        ans.append(x)
print(len(ans))
print(*ans[::-1])