import sys
sys.setrecursionlimit(10**7)


N = int(input())

A = [[] for _ in range(N+1)]
T = [0] * (N+1)
for i in range(1, N+1):
    t, _, *a = map(int, input().split())
    T[i] += t
    A[i] += a

ans = 0
visited = [-1] * (N+1)
def dfs(x):
    global ans
    visited[x] = 1
    ans += T[x]
    for to in A[x]:
        if visited[to] != -1:
            continue
        dfs(to)
dfs(N)
print(ans)