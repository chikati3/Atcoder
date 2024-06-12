H, W = map(int, input().split())
S = [input() for _ in range(H)]
T = [input() for _ in range(H)]

s = [[] for _ in range(W)]
t = [[] for _ in range(W)]
for i in range(H):
  for j in range(W):
    s[j].append(S[i][j])
    t[j].append(T[i][j])

if sorted(s) == sorted(t):
  print('Yes')
else:
  print('No')