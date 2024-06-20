X, Y, N = map(int, input().split())

ans = float('inf')
for i in range(N+1):
  for j in range(N+1):
    if i + j*3 == N:
      ans = min(ans, i*X + j*Y)
print(ans)