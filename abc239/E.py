import sys
sys.setrecursionlimit(10**7)


n, q = map(int, input().split())
x = list(map(int, input().split()))

edge = [[]for _ in range(n)]
for _ in range(n-1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    edge[a].append(b)
    edge[b].append(a)

root = [[] for _ in range(n+1)]

def dfs(u, par):
    root[u].append(x[u])
    for to in edge[u]:
        if to == par:
            continue
        dfs(to, u)
        root[u] += root[to]
        root[u].sort(reverse=True)
        root[u] = root[u][:20]

dfs(0, 0)
for _ in range(q):
    v, k = map(int, input().split())
    v -= 1
    k -= 1
    print(root[v][k])