import sys
sys.setrecursionlimit(10**7)


n, m, q = map(int, input().split())

par = [-1] * (n+1)

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
    par[x] += par[y]
    par[y] = x

edges = []
for _ in range(m):
    u, v, w = map(int, input().split())
    edges.append((w, u, v, -1))
for i in range(q):
    u, v, w = map(int, input().split())
    edges.append((w, u, v, i))
edges.sort()

ans = [False] * q
for _, u, v, ni in edges:
    if find(u) == find(v):
        continue
    if ni != -1:
        ans[ni] = True
    else:
        union(u, v)

for i in range(q):
    if ans[i] == True:
        print('Yes')
    else:
        print('No')