N, M = map(int, input().split())

edge = [[] for _ in range(N)]
for _ in range(M):
    A, B = map(int, input().split())
    A -= 1
    B -= 1
    if B < A:
        A, B = B, A
    edge[A].append(B)

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

ans = [0]
cnt = 0
for i in range(N-1, 0, -1):
    cnt += 1
    for j in edge[i]:
        if find(i) != find(j):
            cnt -= 1
        union(i, j)
    ans.append(cnt)

for i in range(N-1, -1, -1):
    print(ans[i])