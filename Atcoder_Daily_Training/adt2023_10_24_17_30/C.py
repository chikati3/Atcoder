A, B = input().split()

N = min(len(A), len(B))
ans = 'Easy'
for i in range(N):
  c = int(A[~i]) + int(B[~i])
  if 10 <= c:
    ans = 'Hard'
print(ans)