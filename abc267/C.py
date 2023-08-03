n, m = map(int, input().split())
a = list(map(int, input().split()))

cum = [0]
for i in range(n):
    cum.append(cum[-1] + a[i])

num = sum(a[i]*(i+1) for i in range(m))
ans = num
for i in range(m, n):
    num -= cum[i] - cum[i-m]
    num += a[i] * m
    ans = max(ans, num)
print(ans)