from itertools import product


n, x = map(int, input().split())

l = []
for _ in range(n):
    _, *a = map(int, input().split())
    l.append(a)

it = list(product(*l))
ans = 0
for i in it:
    c = 1
    for j in i:
        c *= j
    if x == c:
        ans += 1
print(ans)