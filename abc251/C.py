n = int(input())

cnt = set()
x = []
mx = 0
for i in range(1, n+1):
    s, t = input().split()
    t = int(t)
    if s not in cnt:
        cnt.add(s)
        x.append([t, i])
        mx = max(mx, t)

y = []
for ti, i in x:
    if mx == ti:
        y.append(i)
print(y[0])