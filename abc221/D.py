N = int(input())
AB = [list(map(int, input().split())) for _ in range(N)]

d = {}
for a, b in AB:
    d.setdefault(a, 0)
    d.setdefault(a+b, 0)
    d[a] += 1
    d[a+b] -= 1

ans = [0] * (N+1)
day = sorted(d.keys())
now = 0
cnt = 0
for di in day:
    ans[cnt] += di - now
    cnt += d[di]
    now = di
print(*ans[1:])