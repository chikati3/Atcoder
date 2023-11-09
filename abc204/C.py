from collections import deque


N, M = map(int, input().split())

edge = [[] for _ in range(N)]
for _ in range(M):
    A, B = map(int, input().split())
    A -= 1
    B -= 1
    edge[A].append(B)

ans = 0
for i in range(N):
    d = deque()
    d.append(i)
    dist = [-1] * N
    dist[i] = 0
    ans += 1
    while d:
        x = d.popleft()
        for to in edge[x]:
            if dist[to] != -1:
                continue
            dist[to] = dist[x]
            d.append(to)
            ans += 1
print(ans)