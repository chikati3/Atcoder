N = int(input())
A = list(map(int, input().split()))

ans = [0] * (2*N+1)
a = []
for i in range(N):
  a.append([A[i]-1, i])
a.sort()

for j, i in a:
  ans[i*2] = ans[j-1] + 1
  ans[i*2+1] = ans[j-1] + 1

print(0)
for i in range(len(ans)-1):
  print(ans[i])