import sys
sys.setrecursionlimit(10**7)


n = int(input())
sx, sy, tx, ty = map(int, input().split())
xyr = [list(map(int, input().split())) for _ in range(n)]

n += 2
xyr.append([sx, sy, 0])
xyr.append([tx, ty, 0])

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

def dist(x1, y1, x2, y2):
    return (x1 - x2)**2 + (y1 - y2)**2

for i in range(n):
    for j in range(i+1, n):
        x1, y1, r1 = xyr[i]
        x2, y2, r2 = xyr[j]
        d = dist(x1, y1, x2, y2)
        if (r1 - r2)**2 <= d <= (r1 + r2)**2:
            union(i, j)

if find(n-2) == find(n-1):
    print('Yes')
else:
    print('No')