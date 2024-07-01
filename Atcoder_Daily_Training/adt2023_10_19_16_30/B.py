N = int(input())
S = input()

ans = 'Yes'
for i in range(N-1):
  if S[i] == S[i+1]:
    ans = 'No'
print(ans)