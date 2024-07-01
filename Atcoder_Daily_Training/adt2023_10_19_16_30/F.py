N, K, X = map(int, input().split())
A = list(map(int, input().split()))

A.sort(reverse=True)
for i in range(N):
  if A[i] // X <= K:
    ki = A[i] // X
    K -= ki
    A[i] -= ki * X
  if 0 == K:
    break

A.sort(reverse=True)
for i in range(min(K, N)):
  A[i] = max(A[i] - X, 0)
print(sum(A))