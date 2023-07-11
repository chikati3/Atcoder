# pypy3

from collections import deque


t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    c = list(map(int, input().split()))

    edge = [[] for _ in range(n)]
    for _ in range(m):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        edge[u].append(v)
        edge[v].append(u)

    d = deque()
    d.append((0, n-1))
    dist = [[-1 for _ in range(n)] for _ in range(n)]
    dist[0][n-1] = 0
    while d:
        taka, aoki = d.popleft()
        for ti in edge[taka]:
            for ai in edge[aoki]:
                if dist[ti][ai] == -1 and c[ti] != c[ai]:
                    dist[ti][ai] = dist[taka][aoki] + 1
                    d.append((ti, ai))
    print(dist[n-1][0])