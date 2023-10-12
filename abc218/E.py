import sys
sys.setrecursionlimit(10**7)


N, M = map(int, input().split())

edges = []
for _ in range(M):
    A, B, C = map(int, input().split())
    A -= 1
    B -= 1
    edges.append([C, A, B])
edges.sort()

par = [-1] * N
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

ans = 0
for c, a, b in edges:
    if c < 0 or find(a) != find(b):
        union(a, b)
    else:
        ans += c
print(ans)