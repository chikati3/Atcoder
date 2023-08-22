from heapq import heappop, heappush, heapify


n, m = map(int, input().split())

edge = [[] for _ in range(n)]
for i in range(1, m+1):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    edge[a].append((c, b, i))
    edge[b].append((c, a, i))

ans = []
seen = [False] * n
seen[0] = True
hq = edge[0][:]
heapify(hq)
while hq:
    c, x, i = heappop(hq)
    if seen[x]:
        continue
    ans.append(i)
    
    seen[x] = True
    for ci, to, idx in edge[x]:
        if seen[to]:
            continue
        heappush(hq, (c+ci, to, idx))
print(*ans)