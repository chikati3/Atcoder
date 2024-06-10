from itertools import permutations
from itertools import combinations_with_replacement


N, M = map(int, input().split())
S = [input() for _ in range(N)]
T = set(input() for _ in range(M))

s = len(''.join(S))

c = set()
for i in combinations_with_replacement(list(range(1, 16-s)), N-1):
  if 3 <= s + sum(i) <= 16:
    for j in permutations(i):
      c.add(j)

for i in permutations(S):
  for j in c:

    ans = i[0]
    for k, v in zip(i[1:], j):
      ans += '_' * v
      ans += k
    if ans not in T:
      print(ans)
      exit()
print(-1)