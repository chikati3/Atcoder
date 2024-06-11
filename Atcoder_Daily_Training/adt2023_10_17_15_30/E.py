N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

C = []
for ai in A:
  C.append([ai, 'A'])
for bi in B:
  C.append([bi, 'B'])

C.sort()
a = []
b = []
for i in range(N+M):
  x, ab = C[i]
  if ab == 'A':
    a.append(i+1)
  else:
    b.append(i+1)
print(*a)
print(*b)