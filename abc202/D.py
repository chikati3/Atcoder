A, B, K = map(int, input().split())

def comb(n, r):
    num = 1
    den = 1
    for i in range(r):
        num *= (n - i)
        den *= (r - i)
    return num // den

a = A
b = B
ans = ''

while 0 < a and 0 < b:
    a_comb = comb(a - 1 + b, a - 1)
    if K <= a_comb:
        ans += 'a'
        a -= 1
    else:
        ans += 'b'
        b -= 1
        K -= a_comb
ans += 'a' * a
ans += 'b' * b
print(ans)