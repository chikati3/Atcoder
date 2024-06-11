N, M = map(int, input().split())

m = []
for _ in range(M):
  k = list(map(int, input().split()))
  x = k[1:]
  m.append(x)

ans = 'Yes'
for i in range(1, N+1):
  for j in range(i+1, N+1):
    ok = 0
    for mi in m:
      if i in mi and j in mi:
        ok = 1
    if ok == 0:
      ans = 'No'
print(ans)