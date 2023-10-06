N = input()

n = len(N)
ans = 0
for i in range(2 ** n):
    l = []
    r = []
    for j in range(n):
        if i >> j & 1:
            l.append(N[j])
        else:
            r.append(N[j])
    l.sort(reverse=True)
    r.sort(reverse=True)
    l = ''.join(l)
    r = ''.join(r)
    if l == '' or r == '' or l[0] == '0' or r[0] == '0':
        continue
    ans = max(ans, int(l) * int(r))
print(ans)