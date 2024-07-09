from itertools import combinations


S = [input() for _ in range(9)]

point = []
for i in range(9):
  for j in range(9):
    if S[i][j] == '#':
      point.append([i, j])

ans = 0
for k in list(combinations(point, 4)):
  cnt = set()
  for l in list(combinations(k, 2)):
    x1, y1 = l[0]
    x2, y2 = l[1]
    cnt.add((x1 - x2)**2 + (y1 - y2)**2)
  if len(cnt) == 2:
    ans += 1
print(ans)