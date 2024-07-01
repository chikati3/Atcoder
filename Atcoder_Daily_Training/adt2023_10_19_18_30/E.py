N = int(input())
A = list(map(int, input().split()))

even = []
odd = []
for i in range(N):
  if A[i] % 2 == 0:
    even.append(A[i])
  else:
    odd.append(A[i])
even.sort()
odd.sort()

e = -1
o = -1
if 2 <= len(even):
  e = even[-1] + even[-2]
if 2 <= len(odd):
  o = odd[-1] + odd[-2]
print(max(e, o))