from bisect import bisect_left


N = int(input())
A = list(map(int, input().split()))

sleep = [0]
for i in range(N-1):
  if i % 2 == 0:
    sleep.append(sleep[-1])
  else:
    sleep.append(A[i+1] - A[i] + sleep[-1])

Q = int(input())
for _ in range(Q):
  L, R = map(int, input().split())

  l = bisect_left(A, L)
  r = bisect_left(A, R)
  ans = sleep[r] - sleep[l]

  if l % 2 == 0:
    ans -= L - A[l]
  if r % 2 == 0:
    ans-= A[r] - R

  print(ans)
