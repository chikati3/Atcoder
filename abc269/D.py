import sys
sys.setrecursionlimit(10**7)


n = int(input())
xy = [list(map(int, input().split())) for _ in range(n)]

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

dxy = [[-1, -1], [-1, 0], [0, -1], [0, 1], [1, 0], [1, 1]]

for i in range(n):
    x1, y1 = xy[i]
    for j in range(n):
        if i == j:
            continue
        for dx, dy in dxy:
            if [x1+dx, y1+dy] == xy[j]:
                union(i, j)
ans = 0
for i in range(n):
    if par[i] < 0:
        ans += 1
print(ans)