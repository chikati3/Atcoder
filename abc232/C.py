from itertools import permutations


n, m = map(int, input().split())

taka = [[False]*n for _ in range(n)]
aoki = [[False]*n for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    taka[a][b] = True
    taka[b][a] = True
for _ in range(m):
    c, d = map(int, input().split())
    c -= 1
    d -= 1
    aoki[c][d] = True
    aoki[d][c] = True

ans = 'No'
it = list(permutations(list(range(n))))
for i in it:
    dist = [[False]*n for _ in range(n)]
    for j in range(n):
        for k in range(n):
            dist[i[j]][i[k]] = aoki[j][k]
    if taka == dist:
        ans = 'Yes'
print(ans)