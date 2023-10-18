import sys
sys.setrecursionlimit(10**7)


N = int(input())

edge = [[] for _ in range(N+1)]
for _ in range(N-1):
    A, B = map(int, input().split())
    edge[A].append(B)
    edge[B].append(A)
for i in range(1, N+1):
    edge[i].sort()

ans = []
def dfs(x, par):
    ans.append(x)
    for to in edge[x]:
        if par == to:
            continue
        dfs(to, x)
        ans.append(x)

dfs(1, 0)
print(*ans)