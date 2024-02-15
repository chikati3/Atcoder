H, W = map(int, input().split())
X = [list(map(int, input().split())) for _ in range(H)]

acc = [[0] * (W+1)]
for i in range(H):
    tmp = [0]
    for j in range(W):
        tmp.append(tmp[-1] + X[i][j])
    acc.append(tmp)

for j in range(W+1):
    for i in range(H):
        acc[i+1][j] += acc[i][j]

Q = int(input())
for _ in range(Q):
    A, B, C, D = map(int, input().split())
    A -= 1
    B -= 1
    print(acc[C][D] + acc[A][B] - acc[A][D] - acc[C][B])