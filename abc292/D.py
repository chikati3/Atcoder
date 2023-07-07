import sys
sys.setrecursionlimit(10**7)


n, m = map(int, input().split())

par = [-1] * (n)
def find(x):
    if par[x] < 0:
        return x
    else:
        par[x] = find(par[x])
        return par[x]
def union(x, y):
    x = find(x)
    y = find(y)
    if x == y:
        return
    if par[y] < par[x]:
        x, y = y, x
    par[x] += par[y]
    par[y] = x

edge = [0] * (n)
for _ in range(m):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    if find(u) != find(v):
        union(u, v)
    edge[find(u)] += 1

ans = 'Yes'
for i in range(n):
    if par[i] < 0:
        if -par[i] != edge[i]:
            ans = 'No'
print(ans)