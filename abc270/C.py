import sys
sys.setrecursionlimit(10**7)


n, x, y = map(int, input().split())

edge = [[] for _ in range(n+1)]
for _ in range(n-1):
    u, v = map(int, input().split())
    edge[u].append(v)
    edge[v].append(u)

ans = []
def dfs(x, par=-1):
    ans.append(x)
    for to in edge[x]:
        if to == par:
            continue
        elif to == y:
            ans.append(y)
            print(*ans)
            exit()
        dfs(to, x)
    ans.pop()
dfs(x)