S = input()

n = len(S)
l = 0
r = 0
for i in range(n):
  if S[i] == 'a':
    l += 1
  else:
    break
for i in range(n-1, -1, -1):
  if S[i] == 'a':
    r += 1
  else:
    break

if l > r:
  print('No')
  exit()

S = S[l:n-r]
if S == S[::-1]:
  print('Yes')
else:
  print('No')