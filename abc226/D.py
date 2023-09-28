from math import gcd


N = int(input())
xy = [list(map(int, input().split())) for _ in range(N)]

ans = set()
for i in range(N):
    x1, y1 = xy[i]
    for j in range(N):
        if i == j:
            continue
        x2, y2 = xy[j]
        xi, yi = x1-x2, y1-y2

        g = gcd(xi, yi)
        ans.add((xi//g, yi//g))
print(len(ans))