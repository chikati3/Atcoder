N = int(input())
S = input()

x, y = 0, 0
xy = set()
xy.add((x, y))
ans = 'No'
for i in range(N):
  si = S[i]
  if si == 'R':
    x += 1
  elif si == 'L':
    x -= 1
  elif si == 'U':
    y += 1
  elif si == 'D':
    y -= 1
  
  if (x, y) in xy:
    ans = 'Yes'
  
  xy.add((x, y))
print(ans)