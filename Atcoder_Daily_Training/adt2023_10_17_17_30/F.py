S = input()
T = input()

S = S + '@'
N = len(T)
for i in range(N):
  if S[i] != T[i]:
    print(i + 1)
    break