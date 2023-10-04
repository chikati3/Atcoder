from heapq import heappop, heappush


N, M = map(int, input().split())

edge = [[] for _ in range(N)]
cnt = [0] * N
for _ in range(M):
    A, B = map(int, input().split())
    A -= 1
    B -= 1
    edge[A].append(B)
    cnt[B] += 1

pq = []
for i in range(N):
    if cnt[i] == 0:
        heappush(pq, i)

ans = []
while pq:
    x = heappop(pq)
    ans.append(x + 1)
    for e in edge[x]:
        cnt[e] -= 1
        if cnt[e] == 0:
            heappush(pq, e)
if len(ans) == N:
    print(*ans)
else:
    print(-1)