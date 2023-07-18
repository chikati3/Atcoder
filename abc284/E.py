import sys
sys.setrecursionlimit(10**7)


n, m = map(int, input().split())

edge = [[] for _ in range(n)]
for _ in range(m):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    edge[u].append(v)
    edge[v].append(u)

ans = 0
path = set()
def dfs(x):
    global ans, path
    path.add(x)
    ans += 1
    if 10**6 <= ans:
        print(ans)
        exit()
    for to in edge[x]:
        if to not in path:
            dfs(to)
    path.discard(x)
dfs(0)
print(ans)