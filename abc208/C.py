N, K = map(int, input().split())
a = list(map(int, input().split()))

idx = []
for i in range(N):
    idx.append([a[i], i, K//N])
idx.sort()

K %= N
for i in range(K):
    idx[i][2] += 1
idx = sorted(idx, key=lambda x : x[1])

for i in range(N):
    print(idx[i][2])