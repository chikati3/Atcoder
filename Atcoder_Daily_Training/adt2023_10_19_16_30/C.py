H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]

B = [[] for _ in range(W)]
for i in range(H):
  for j in range(W):
    B[j].append(A[i][j])

for b in B:
  print(*b)