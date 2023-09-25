Q = int(input())

n = 2 ** 20
A = [-1] * n
par = [i for i in range(n)]

def find(x):
    if par[x] == x:
        return x
    par[x] = find(par[x])
    return par[x]

for i in range(Q):
    t, x = map(int, input().split())
    if t == 1:
        h = find(x%n)
        A[h] = x
        par[h] = (h+1) % n
    elif t == 2:
        print(A[x%n])