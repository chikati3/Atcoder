# pypy3
# 包除原理

n, m = map(int, input().split())
mod = 998244353

fact = [1] * (n+1)
inv = [1] * (n+1)
finv = [1] * (n+1)
for i in range(2, n+1):
    fact[i] = fact[i - 1] * i % mod
    inv[i] = mod - inv[mod % i] * (mod // i) % mod
    finv[i] = finv[i - 1] * inv[i] % mod
def comb(a, b):
    return (fact[a] * finv[b] % mod) * finv[a - b] % mod

ans = 0
for i in range(n+1):
    ans += (-1 if i%2 else 1) * pow(m, max(1, n-i), mod) * comb(n, i) % mod
print(ans % mod)