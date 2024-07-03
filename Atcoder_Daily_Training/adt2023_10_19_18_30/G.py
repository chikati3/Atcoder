from collections import deque


N, M = map(int, input().split())

A = []
for _ in range(M):
  K = int(input())
  a = list(map(int, input().split()))
  d = deque()
  for ai in a:
    d.append(ai)
  A.append(d)

color = [0] * (N+1)
color_idx = [[] for _ in range(N+1)]
balls = deque()
cnt = set()

def f(idx):
  ball = A[idx].popleft()
  color[ball] += 1
  color_idx[ball].append(idx)
  if color[ball] == 2:
    balls.append(ball)
  if len(A[idx]) == 0:
    cnt.add(idx)

for i in range(M):
  f(i)

while balls:
  x = balls.popleft()
  x1, x2 = color_idx[x]
  if 1 <= len(A[x1]):
    f(x1)
  if 1 <= len(A[x2]):
    f(x2)

if len(cnt) == M:
  print('Yes')
else:
  print('No')