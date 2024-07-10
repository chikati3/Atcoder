N, M, X, T, D = map(int, input().split())

day = [0] * (N+1)
for i in range(X, N+1):
  day[i] = T
for i in range(X-1, -1, -1):
  day[i] = day[i+1] - D
print(day[M])  