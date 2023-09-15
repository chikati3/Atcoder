N, Q = map(int, input().split())
a = list(map(int, input().split()))

d = {}
for i in range(N):
    d.setdefault(a[i], [0])
    d[a[i]].append(i+1)

for _ in range(Q):
    x, k = map(int, input().split())
    if x not in d or len(d[x]) <= k:
        print(-1)
    else:
        print(d[x][k])