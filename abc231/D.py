import sys
sys.setrecursionlimit(10**7)


N, M = map(int, input().split())

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
    par[x] += par[y]
    par[y] = x

cnt = [0] * N
ans = 'Yes'
for _ in range(M):
    A, B = map(int, input().split())
    A -= 1
    B -= 1

    cnt[A] += 1
    cnt[B] += 1
    if find(A) == find(B):
        ans = 'No'
    union(A, B)

if 2 < max(cnt):
    ans = 'No'
print(ans)