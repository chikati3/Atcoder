S = list(map(int, input().split()))
N = len(S)

ans = 'Yes'
for i in range(N-1):
  if S[i] > S[i+1]:
    ans = 'No'

for i in range(N):
  if S[i] < 100 or 675 < S[i]:
    ans = 'No'
  if S[i] % 25  != 0:
    ans = 'No'

print(ans)