from itertools import permutations


S, K = input().split()
k = int(K)

s = list(S)
it = list(permutations(s))
x = set()
for i in it:
    i = ''.join(i)
    x.add(i)
x = sorted(x)
print(x[k-1])