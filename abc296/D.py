
n, m = map(int, input().split())

INF = 10**18
ans = INF
for a in range(1, m+1):
    b = -(-m//a)
    if b < a:
        break
    if b <= n:
        ans = min(ans, a*b)
if ans == INF:
    print(-1)
else:
    print(ans)