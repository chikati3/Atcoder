S = input()
N = len(S)

x = 'atcoder'
s = []
for i in range(N):
  s.append(x.index(S[i]))

cnt = 0
while s != sorted(s):
  for i in range(N-1):
    if s[i] > s[i+1]:
      s[i], s[i+1] = s[i+1], s[i]
      cnt += 1
print(cnt)