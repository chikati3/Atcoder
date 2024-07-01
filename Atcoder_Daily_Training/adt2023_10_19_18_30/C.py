S = input()

up = [0] * 26
low = [0] * 26
for si in S:
  if 65 <= ord(si) <= 65+25:
    up[ord(si) % 65] += 1
  else:
    low[ord(si) % 97] += 1

if max(up) == 1 and max(low) == 1:
  print('Yes')
else:
  print('No')