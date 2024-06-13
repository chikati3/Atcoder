N = int(input())
S = [input() for _ in range(N)]

ans = 'No'
for i in range(N):
  for j in range(N):
    if i == j:
      continue
    x = S[i] + S[j]
    if x == x[::-1]:
      ans = 'Yes'
print(ans)