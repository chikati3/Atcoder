S = input()

if S[0] == '1':
  print('No')
  exit()

x = [[6], [3], [7, 1], [4, 0], [8, 2], [5], [9]]
T = [0] * 7
for i in range(len(x)):
  for j in x[i]:
    if S[j] == '1':
      T[i] = 1

for i in range(3, 8):
  for j in range(len(T)-i+1):
    t = T[j:j+i]
    if t[0] == 1 and t[-1] == 1 and t.count(1) == 2:
      print('Yes')
      exit()
print('No')