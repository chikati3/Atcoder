N = int(input())
xy = [list(map(int, input().split())) for _ in range(N)]

def f(a, b, c):
    return (b[0] - a[0]) * (c[1] - a[1]) != (b[1] - a[1]) * (c[0] - a[0])

ans = 0
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            if f(xy[i], xy[j], xy[k]):
                ans += 1
print(ans)