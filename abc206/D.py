import sys
sys.setrecursionlimit(10**7)


N = int(input())
A = list(map(int, input().split()))

par = [-1] * (2*10**5+1)
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
for i in range(N//2):
    a = A[i] - 1
    b = A[~i] - 1
    if find(a) != find(b):
        union(a, b)
        ans += 1
print(ans)