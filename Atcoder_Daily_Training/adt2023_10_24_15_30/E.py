N, Q = map(int, input().split())
a = list(map(int, input().split()))

cnt = {}
for i in range(N):
  cnt.setdefault(a[i], [])
  cnt[a[i]].append(i+1)

for _ in range(Q):
  x, k = map(int, input().split())
  if x in cnt and k <= len(cnt[x]):
    print(cnt[x][k-1])
  else:
    print(-1)