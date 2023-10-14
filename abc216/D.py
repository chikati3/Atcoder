from collections import deque


N, M = map(int, input().split())

cnt = [0] * (N+1)
edge = [[] for _ in range(N+1)]
for _ in range(M):
    k = int(input())
    a = list(map(int, input().split()))
    for i in range(k-1):
        edge[a[i]].append(a[i+1])
        cnt[a[i+1]] += 1

d = deque()
for i in range(1, N+1):
    if cnt[i] == 0:
        d.append(i)

while d:
    x = d.popleft()
    for to in edge[x]:
        cnt[to] -= 1
        if cnt[to] == 0:
            d.append(to)

if max(cnt[1:]) == 0:
    print('Yes')
else:
    print('No')