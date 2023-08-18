n, k = map(int, input().split())
a = list(map(int, input().split()))

m = [[] for _ in range(k)]
idx = [[] for _ in range(k)]
for i in range(n):
    m[i%k].append(a[i])
    idx[i%k].append(i)
for i in m:
    i.sort()

cnt = [0]*n
for i, j in zip(idx, m):
    for v in range(len(i)):
        cnt[i[v]] = j[v]

ans = 'Yes'
for i in range(n-1):
    if cnt[i] > cnt[i+1]:
        ans = 'No'
print(ans)