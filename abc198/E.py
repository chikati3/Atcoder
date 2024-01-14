import sys 
sys.setrecursionlimit(10**7)


N = int(input())
C = list(map(int, input().split()))

edge = [[] for _ in range(N)]
for _ in range(N-1):
    A, B = map(int, input().split())
    A -= 1
    B -= 1
    edge[A].append(B)
    edge[B].append(A)

colors = [0] * 10**6
ans = []

def dfs(now, par):
    x = colors[C[now]]
    if not x:
        colors[C[now]] = 1
        ans.append(now+1)
    
    for to in edge[now]:
        if to != par:
            dfs(to, now)
    if not x:
        colors[C[now]] = 0

dfs(0, -1)
ans.sort()
for i in ans:
    print(i)