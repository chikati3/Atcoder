import sys
sys.setrecursionlimit(10**7)


def find(x):
    if par[x] == x:
        return x
    else:
        par[x] = find(par[x])
        return par[x]
def union(x, y):
    x = find(x)
    y = find(y)
    if x == y:
        return 0
    par[x] = y


n = int(input())
st = [input().split() for _ in range(n)]

par = {}
for i in range(n):
    s, t = st[i]
    par[s] = s
    par[t] = t

for i in range(n):
    s, t = st[i]
    if find(s) == find(t):
        print('No')
        exit()
    union(s, t)
print('Yes')