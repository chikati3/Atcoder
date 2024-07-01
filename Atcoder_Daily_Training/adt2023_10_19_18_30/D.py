N, M, T = map(int, input().split())
A = list(map(int, input().split()))

A.append(0)

x = {}
for i in range(M):
  X, Y = map(int, input().split())
  X -= 1
  x.setdefault(X, Y)

ans = 'Yes'
for i in range(N):
  if i in x:
    T += x[i]
  if 0 < T - A[i]:
    T -= A[i]
  elif T - A[i] <= 0:
    ans = 'No'
    break
print(ans)
