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
  if par[x] > par[y]:
    x, y = y, x
  par[x] += par[y]
  par[y] = x

for _ in range(M):
  u, v = map(int, input().split())
  u -= 1
  v -= 1
  union(u, v)

ans = 0
for i in range(N):
  if par[i] < 0:
    ans += 1
print(ans)