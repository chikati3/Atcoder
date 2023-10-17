import sys
sys.setrecursionlimit(10**7)


N = int(input())

cost = []
for _ in range(N-1):
    u, v, w = map(int, input().split())
    u -= 1
    v -= 1
    cost.append([w, u, v])
cost.sort()

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
for w, u, v in cost:
    ans += par[find(u)] * par[find(v)] * w
    union(u, v)
print(ans)
