n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))
x = int(input())

dp = [None] * (x + 1)
dp[0] = True
for bi in b:
    dp[bi] = False

for i in range(x+1):
    if dp[i] == True:
        for ai in a:
            if i + ai <= x and dp[i+ai] != False:
                dp[i+ai] = True
if dp[x] == True:
    print('Yes')
else:
    print('No')