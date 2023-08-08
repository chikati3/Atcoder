from itertools import combinations


h1, w1 = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(h1)]
h2, w2 = map(int, input().split())
b = [list(map(int, input().split())) for _ in range(h2)]

for i in combinations(range(h1), h2):
    for j in combinations(range(w1), w2):
        x = [[a[c][d] for d in j] for c in i]
        if b == x:
            print('Yes')
            exit()
print('No')