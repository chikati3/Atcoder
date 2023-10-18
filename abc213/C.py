from bisect import bisect_left


H, W, N = map(int, input().split())

x = set()
y = set()
xy = []
for _ in range(N):
    a, b = map(int, input().split())
    y.add(a)
    x.add(b)
    xy.append([a, b])
y = sorted(y)
x = sorted(x)

for yi, xi in xy:
    by = bisect_left(y, yi) + 1
    bx = bisect_left(x, xi) + 1
    print(by, bx)