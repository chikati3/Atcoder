N = int(input())

def f():
    a = set()
    for i in range(N):
        x = input()
        for j in range(N):
            if x[j] == '#':
                a.add((i, j))
    return a

S = f()
T = f()

for _ in range(4):
    ys, xs = min(S)
    yt, xt = min(T)

    S = set((y-ys, x-xs) for y, x in S)
    T = set((y-yt, x-xt) for y, x in T)

    if S == T:
        print('Yes')
        exit()
    T = set((-x, y) for y, x in T)
print('No')