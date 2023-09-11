n = int(input())

def f(a, z):
    return (a + z) * (z-a+1) // 2

mod = 998244353
ans = 0
rx = 0
for i in range(1, 19):
    l = 10**(i-1)
    r = 10**i-1
    if r <= n:
        ans += f(l-rx, r-rx)
    elif l <= n <= r:
        ans += f(l-rx, min(r, n) - rx)
    rx = r
    ans %= mod
print(ans)