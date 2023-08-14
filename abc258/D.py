n, x = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

cum = [0]
for i in range(n):
    cum.append(cum[-1] + sum(a[i]))

ans = float('inf')
for i in range(1, n+1):
    cnt = cum[i] + a[i-1][1] * max(0, x - i)
    ans = min(ans, cnt)
print(ans)