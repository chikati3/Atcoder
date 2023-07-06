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

x = 0
for _ in range(m):
    a, b, c, d = input().split()
    a = int(a) - 1
    c = int(c) - 1

    # 閉路数
    if find(a) == find(c):
        x += 1
    union(a, c)

# グループ数
y = 0
for i in range(n):
    if par[i] < 0:
        y += 1
print(x, y-x)