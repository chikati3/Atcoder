n, m = map(int, input().split())

edge = [[] for _ in range(n)]
cnt = [0] * n
for _ in range(m):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    edge[x].append(y)
    cnt[y] += 1

d = []
for i in range(n):
    if cnt[i] == 0:
        d.append(i)

now = 1
ans = [0] * n
while d:
    if 1 < len(d):
        print('No')
        exit()
    x = d.pop()
    ans[x] = now
    now += 1
    for to in edge[x]:
        cnt[to] -= 1
        if cnt[to] == 0:
            d.append(to)

if now == n+1:
    print('Yes')
    print(*ans)
else:
    print('No')