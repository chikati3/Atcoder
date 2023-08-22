n = int(input())
a = list(map(int, input().split()))

def comb(n, r):
    num = 1
    den = 1
    for i in range(r):
        num *= (n - i)
        den *= (r - i)
    return num // den

cnt = {}
for ai in a:
    cnt.setdefault(ai, 0)
    cnt[ai] += 1

ans = comb(n, 3)
for k in cnt:
    v = cnt[k]
    ans -= comb(v, 3)
    ans -= comb(v, 2) * (n-v)
print(ans)