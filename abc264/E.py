import sys
sys.setrecursionlimit(10**7)


n, m, e = map(int, input().split())

uv = []
for _ in range(e):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    uv.append([u, v])

q = int(input())
x = []
xs = set()
for _ in range(q):
    xi = int(input())
    xi -= 1
    x.append(xi)
    xs.add(xi)

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
    if par[y] < par[x]:
        x, y = y, x
    par[x] += par[y]
    par[y] = x

for i in range(e):
    if i not in xs:
        u, v = uv[i]
        union(min(u, n), min(v, n))

cnt = 0
for i in range(n):
    if find(i) == find(n):
        cnt += 1

ans = []
ans.append(cnt)
for i in range(q-1, 0, -1):
    xi = x[i]
    u, v = uv[xi]
    u = min(u, n)
    v = min(v, n)

    if n == u and n == v:
        ans.append(cnt)
        continue

    fu = find(u)
    fv = find(v)
    fn = find(n)
    if fu == fn and fv == fn:
        ans.append(cnt)
        continue
    
    if fu != fn and fv == fn:
        cnt += par[fu] * -1
    if fu == fn and fv != fn:
        cnt += par[fv] * -1
    
    ans.append(cnt)
    union(min(u, n), min(v, n))

for i in ans[::-1]:
    print(i)