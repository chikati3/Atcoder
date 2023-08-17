from bisect import bisect_left


n, q = map(int, input().split())
a = list(map(int, input().split()))

a.sort()

cum = [0]
for ai in a:
    cum.append(cum[-1] + ai)

for _ in range(q):
    x = int(input())
    b = bisect_left(a, x)
    l = b*x
    r = (n-b) * x
    print(l-cum[b] + cum[n] - cum[b] - r)