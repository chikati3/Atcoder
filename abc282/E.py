import sys
sys.setrecursionlimit(10**7)


n, m = map(int, input().split())
a = list(map(int, input().split()))

par = [-1] * n
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

def f(x, y, m):
    return (pow(x, y, m) + pow(y, x, m)) % m
cost = []
for i in range(n):
    for j in range(i+1, n):
        cost.append((-f(a[i], a[j], m), i, j))
cost.sort(reverse=True)

ans = 0
while 2 <= len(cost):
    c, i, j = cost.pop()  
    if find(i) != find(j):
        union(i, j)
        ans -= c
print(ans)