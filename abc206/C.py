N = int(input())
A = list(map(int, input().split()))

def f(x):
    return x * (x - 1) // 2

ans = f(N)
cnts = {}
for a in A:
    cnts.setdefault(a, 0)
    cnts[a] += 1

for c in cnts:
    ans -= f(cnts[c])
print(ans)