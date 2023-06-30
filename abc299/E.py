
from collections import deque


n, m = map(int, input().split())

edge = [[] for _ in range(n)]
for _ in range(m):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    edge[u].append(v)
    edge[v].append(u)

k = int(input())
pd = [-1 for _ in range(n)]
for _ in range(k):
    p, d = map(int, input().split())
    p -= 1
    pd[p] = d

def bfs(i):
    dist = [-1] * n
    dist[i] = 0
    d = deque()
    d.append(i)
    while d:
        x = d.popleft()
        for to in edge[x]:
            if dist[to] != -1:
                continue
            dist[to] = dist[x] + 1
            d.append(to)
    return dist

ans = [pd[i] == -1 for i in range(n)]
s = [0] * n
for i in range(n):
    b = bfs(i)
    if all(pd[j] <= b[j] for j in range(n)):
        s[i] = 1
        for w in range(n):
            ans[w] |= b[w] == pd[w]
if all(ans):
    print('Yes')
    print(''.join(map(str, s)))
else:
    print('No')