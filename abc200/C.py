from collections import defaultdict


N = int(input())
A = list(map(int, input().split()))

d = defaultdict(int)
for a in A:
    d[a%200] += 1

def f(x):
    return x * (x - 1) // 2

ans = 0
for k in d:
    ans += f(d[k])
print(ans)