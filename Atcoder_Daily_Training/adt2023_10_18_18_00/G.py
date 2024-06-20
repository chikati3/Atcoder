N, X = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(N)]

time = 0
ans = float('inf')
for i in range(N):
  a, b = AB[i]
  time += a + b
  X -= 1
  ans = min(ans, time + b * X)
  if X == 0:
    break

print(ans)