H, W, N = map(int, input().split())

field = [[0]*(W+1) for _ in range(H+1)]
for _ in range(N):
    A, B, C, D = map(int, input().split())
    A -= 1
    B -= 1
    field[A][B] += 1
    field[A][D] -= 1
    field[C][B] -= 1
    field[C][D] += 1

for i in range(H):
    for j in range(W):
        field[i][j+1] += field[i][j]

for j in range(W):
    for i in range(H):
        field[i+1][j] += field[i][j]

for f in field[:-1]:
    print(*f[:-1])