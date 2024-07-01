S = input()
N = len(S)

for i in range(N):
  if 65 <= ord(S[i]) <= 65+25:
    print(i+1)
    break