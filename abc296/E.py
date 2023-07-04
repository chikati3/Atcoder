
import sys
sys.setrecursionlimit(10**7)


n = int(input())
a = [int(i)-1 for i in input().split()]

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

ans = 0
for i in range(n):
    if find(i) != find(a[i]):
        union(i, a[i])
    else:
        ai = a[i]
        ans += 1
        while i != ai:
            ans += 1
            ai = a[ai]
print(ans)