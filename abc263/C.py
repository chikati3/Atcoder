from itertools import combinations


n, m = map(int, input().split())

it = list(combinations(list(range(1, m+1)), n))
for i in it:
    print(*i)