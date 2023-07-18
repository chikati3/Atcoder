from collections import deque


n, m = map(int, input().split())

edge = [[] for _ in range(n)]
s = []
for _ in range(m):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    edge[u].append(v)
    edge[v].append(u)
    s.append((u, v))

ans = n * (n-1) // 2
flip = [-1] * n
for i in range(n):
    if flip[i] != -1:
        continue
    
    flip[i] = 0
    o, l = 1, 0
    d = deque()
    d.append(i)
    while d:
        x = d.popleft()
        for to in edge[x]:
            if flip[to] != -1:
                continue
            flip[to] = 1 - flip[x]
            d.append(to)

            if flip[to] == 0:
                o += 1
            else:
                l += 1
    ans -= o * (o-1) // 2
    ans -= l * (l-1) // 2
for u, v in s:
    if flip[u] == flip[v]:
        print(0)
        exit()
print(ans - m)